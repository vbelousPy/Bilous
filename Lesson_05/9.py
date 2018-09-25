import sys


def parse_args():
    my_args = sys.argv
    i = 1
    my_dict = {"args": []}
    while i < len(my_args):
        if my_args[i].find("--") == -1:
            my_dict.get("args").append(my_args[i])
            i += 1
        else:
            try:
                my_dict.update({my_args[i]: my_args[i + 1]})
                i += 2
            except IndexError:
                print("Incorrect last argument")
                break

    return my_dict


print(parse_args())
