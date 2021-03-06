# Interrupt Handler
Interrupt Handling Util for Python.

## Installation
```bash
$ pip install InterruptHandler
```

## How to Use
```python
from interrupt_handler import InterruptHandler

# Break by Keyboard Interrupt (Default)
with InterruptHandler() as h:
  ...
  
# Break by checking interrupted flag.
with InterruptHandler(lambda: True) as h:
  if h.interrupted:
    break
  ...
  
 
# Propagate signal to parent.
with InterruptHandler():
  with InterruptHandler(propagate=True):
    ...
```
  
### Callback customize
#### return False
> Escape 'with statement' forcley.
#### return True
> Switch 'interrupted flag'.
``` python
def callback():
  print('Interrupted by User.')
  return False
  
with InterruptHandler(callback) as h:
  ...
```

## Example
```python
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
```
