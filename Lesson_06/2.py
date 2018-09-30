class ProgLanguage:

    def build(self):
        raise NotImplementedError("Please Implement this method")


class CompiledLanguage(ProgLanguage):

    def compile(self):
        print("compile")

    def build(self):
        self.compile()


class InterpretedLanguage(ProgLanguage):

    def interpret(self):
        print("interpret")

    def build(self):
        self.interpret()


CPP = CompiledLanguage()
Python = InterpretedLanguage()

classList = [CPP, Python]
for some_class in classList:
    some_class.build()
