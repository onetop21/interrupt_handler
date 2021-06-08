import time
from interrupt_handler import InterruptHandler, default_callback

if __name__ == '__main__':
    import time
    main_loop = True
    sub_loop = True
    with InterruptHandler(default_callback('Locked', True)) as h1:
        while not h1.interrupted:
            print(f'MainLoop {time.time()}, {h1}, {h1.interrupted}')
            with InterruptHandler(default_callback('Message2')) as h2:
                while sub_loop:
                    print(f'SubLoop {time.time()}')
                    time.sleep(1)
            sub_loop = False
            time.sleep(1)
    main_loop = False