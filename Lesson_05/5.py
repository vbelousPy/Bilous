def foo(*args, **kwargs):
    my_list = list(args)
    for i in range(len(my_list)):
        my_list[i] = my_list[i] + 1
    my_dict = kwargs
    for key in my_dict.keys():
        my_dict.update({key: my_dict.get(key) + 1})
    return my_list, my_dict


def runner(some_func, *args, **kwargs):
    return some_func(*args, **kwargs)


try:
    print(runner(foo, 1, 2, 3, a=4, b=5))
except:
    print("error")
