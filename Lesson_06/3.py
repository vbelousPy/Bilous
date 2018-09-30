class KeyChain(dict):

    def set(self, usr, passwd):
        super().update({usr: passwd})

    def remove(self, key):
        super().pop(key)


my_chain = KeyChain()
my_chain.set("guest", "0000")
print(my_chain)
print(my_chain.get("guest"))
my_chain.remove("guest")
print(my_chain)