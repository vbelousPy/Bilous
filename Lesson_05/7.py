def custom():
    print("some_func")


def make(action, func=None):
    if action == "print":
        return print
    elif action == "input":
        return input
    elif action == "custom":
        if func is None:
            raise KeyError
        else:
            return func


foo = make("custom", custom)
foo()
