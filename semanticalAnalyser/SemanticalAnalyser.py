from .ExpCodeGenerator import ExpCodeGenerator
from .CodeGenerator import CodeGenerator

class SemanticalAnalyser:
    def __init__(self):
        self.expCodeGenerator = ExpCodeGenerator()
        self.codeGenerator = CodeGenerator()
        self.tokens = []

    def generateCode(self, tokens):
        # This code will only generate code for the aritimetical expression

        formattedTokens = tokens[1:]     # removing the first token, just the line identifier
        for token in formattedTokens:  
            # transition the automous. If error, will raise an error
            self.expCodeGenerator.transition(token)

            print(self.expCodeGenerator.elementStack)

        self.codeGenerator.addCodeLines(self.expCodeGenerator.codeLines)
        self.codeGenerator.printCode()

        return True