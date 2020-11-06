from .LexicalAnalyserAutomous import LexicalAnalyserAutomous
from .Token import Token
import re

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

        tokens = self.refineTokens(tokens)
        return tokens
        
    def refineTokens(self, tokens):
        for index, token in enumerate(tokens):
            if (self.isVar(token)):
                token.type == "VAR"
            elif (self.isEnd(token)):
                token.type == "END"
            elif (self.isPredef(token)):
                token.type == "PREDEF"
                
        return tokens


    def removeSpacesAndNewLines(self, string):
        return string.strip().replace(" ", "")
    
    def isVar(self, token):
        if(token.type == "ID"):
            match = re.match("^[A-Z][0-9]$", token.value)
            if(match):
                return True
        return False
        
    def isEnd(self, token):
        if(token.type == "ID"):
            if(token.value == "END"):
                return True
        return False

    def isPredef(self, token):
        if(token.type == "ID"):
            if(token.value == "SEN"):
                return True
        return False
