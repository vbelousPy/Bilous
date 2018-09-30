class ProgLanguage:

    def build(self):
        raise NotImplementedError("Please Implement this method")

    def get_name(self):
        raise NotImplementedError("Please Implement this method")

    def name(self):
        return self.__class__.__name__


class CompiledLanguage(ProgLanguage):

    def compile(self):
        print("compile")

    def build(self):
        self.compile()

    def get_name(self):
        return "CompiledLanguage"


class InterpretedLanguage(ProgLanguage):

    def interpret(self):
        print("interpret")

    def build(self):
        self.interpret()

    def get_name(self):
        return "InterpretedLanguage"


CPP = CompiledLanguage()
Python = InterpretedLanguage()

classList = [CPP, Python]
for some_class in classList:
    print(some_class.name())
