import sys
import os
import signal
from .default_callback import default_callback

class InterruptHandler(object):

    DEFAULT_HANDLERS = {s: signal.getsignal(s) for s in signal.Signals}

    def __init__(self, callback=default_callback(), sig=signal.SIGINT, propagate=False):
        if not callable(callback):
            raise ValueError(f'callback parameter is not support {type(callback)}.')
        self.callback = callback
        self.sig = sig
        self.propagate = propagate
        self.original_handler = signal.getsignal(self.sig)

    @property
    def interrupted(self):
        return getattr(self, '_interrupted', False)

    def __enter__(self):
        self.initialize()
        return self

    def __exit__(self, type, value, tb):
        return self.release()

    def initialize(self):
        if not self.original_handler:
            self._interrupted = False
            self.released = False
            def handler(signum, frame):
                if not self.callback():
                    self.release(True)
                self._interrupted = True
            signal.signal(self.sig, handler)
        else:
            raise RuntimeError('Already initialized.')

    def release(self, interrupted=False):
        if self.released:
            if self.propagate and self.original_handler != self.DEFAULT_HANDLERS[self.sig]:
                os.kill(os.getpid(), self.sig)
            return True
        if self.original_handler:
            signal.signal(self.sig, self.original_handler)
        self.released = True
        if interrupted: raise KeyboardInterrupt
        return False
