import signal

# Raise an exception to unfreeze the thread after calling input()
def alarm_handler():
    raise Exception

def input_with_timeout(prompt, timeout):
    # set signal handler
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout) # produce SIGALRM in `timeout` seconds

    try:
        return input(prompt)
    except Exception as ex:
        pass
    finally:
        signal.alarm(0) # cancel alarm