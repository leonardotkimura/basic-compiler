from .LexicalAnalyserAutomous import LexicalAnalyserAutomous
from .Token import Token

class LexicalAnalyser:
    def __init__(self):
        self.automous = LexicalAnalyserAutomous()
        self.tokens = []

    def execute(self, text):
        tokens = []
        tokenString = ""

        for char in text:
            result = self.automous.transition(char)
            if (result == "ID"):
                tokens.append(Token("ID", tokenString))
                tokenString = ""
            if (result == "NUMBER"):
                tokens.append(Token("NUMBER", tokenString))
                tokenString = ""
            if (result == "SPECIAL"):
                tokens.append(Token("SPECIAL", tokenString))
                tokenString = ""
            if (result == "STRING"):
                tokens.append(Token("STRING", tokenString))
                tokenString = ""
            else:
                tokenString += char
                tokenString = self.removeSpacesAndNewLines(tokenString)

    
        return tokens
    
    def removeSpacesAndNewLines(self, string):
        return string.strip().replace(" ", "")
