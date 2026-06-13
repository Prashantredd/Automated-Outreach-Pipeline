from time import sleep

def retry(func):
    for _ in range(3):
        try:
            return func()
        except Exception:
            sleep(2)