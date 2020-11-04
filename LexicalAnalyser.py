from LexicalAnalyserAutomous import LexicalAnalyserAutomous
from Token import Token

class LexicalAnalyser:
    def __init__(self):
        self.automous = LexicalAnalyserAutomous()
        self.tokens = []

    def execute(self, lines):
        tokens = []
        tokenString = ""

        for line in lines: 
            for char in line:
                result = self.automous.transition(char)
                if (result == "ID"):
                    tokens.append(Token("ID", tokenString))
                    tokenString = ""
                else:
                    tokenString += char

        
        return tokens
