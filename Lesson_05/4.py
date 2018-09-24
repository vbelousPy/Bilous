import random

import string


def password_generator(i, use_caps=False, use_digits=False):
    password_symbol = string.ascii_lowercase
    if use_caps:
        password_symbol += string.ascii_uppercase
    if use_digits:
        password_symbol += string.digits
    passwd = ""
    while i > 0:
        passwd += random.choice(password_symbol)
        i -= 1
    return passwd


print(password_generator(12, use_caps=True, use_digits=True))
