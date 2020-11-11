from .ExpCodeGenerator import ExpCodeGenerator
from .CodeGenerator import CodeGenerator

class SemanticalAnalyser:
    def __init__(self):
        self.expCodeGenerator = ExpCodeGenerator()
        self.codeGenerator = CodeGenerator()
        self.tokens = []

    def generateCode(self, tokens):
        # This code will only generate code for the aritimetical expression

        tokens = tokens[1:]     # removing the first token, just the line identifier
        # for token in tokens:  
        #     # transition the automous. If error, will raise an error
        #     self.expCodeGenerator.transition(token)
        #     print("token: {} , state: {} ".format(token.value, self.automous.state))

        self.codeGenerator.printCode()

        return True