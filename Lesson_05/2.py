import time


def foo():
    while True:
        try:
            print("Hey Apple!")
            time.sleep(5)
        except KeyboardInterrupt:
            continue


foo()
