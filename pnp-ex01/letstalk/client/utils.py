import msvcrt
import time
import sys

# https://stackoverflow.com/questions/15528939/python-3-timed-input 
def input_with_timeout(prompt, timeout):
    userInput = None
    try:
        userInput = get_input(prompt, timeout)
    except TimeoutExpired:
        pass

    return userInput
    

def get_input(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():  # msvcrt.kbhit() returns True if a keypress is waiting to be read.
            result.append(msvcrt.getwche())  # We read a keyspress. More details can be found at https://docs.python.org/3/library/msvcrt.html#msvcrt.getche
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # give other processes/threads to read the keystroke, if needed
    raise TimeoutExpired