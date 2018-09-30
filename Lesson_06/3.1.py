import base64


class KeyChain(dict):

    def set(self, usr, passwd):
        super().update({usr: self._encode(passwd)})

    def remove(self, key):
        super().pop(key)

    def get(self, key):
        return self._decode(super().get(key))

    def _encode(self, passwd):
        return base64.b64encode(passwd.encode())

    def _decode(self, passwd):
        return base64.b64decode(passwd).decode()


my_chain = KeyChain()
my_chain.set("guest", "0000")
print(my_chain)
print("guest =", my_chain.get("guest"))
