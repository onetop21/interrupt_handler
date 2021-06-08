import sys

def default_callback(message='Aborted.', blocked=False):
    def wrapper():
        print(message, file=sys.stderr)
        return blocked
    return wrapper