import re

class LexicalAnalyserAutomous:
    def __init__(self):
        self.state = 1

    def transition(self, char):
        if (self.state == 1):
            if (self.isLetter(char)):
                self.state = 2
            if (self.isDigit(char)):
                self.state = 3
            if (self.isSingleSpecial(char)):
                self.state = 4
            if (self.isQuote(char)):
                self.state = 5
            if (self.isDoubleSpecial(char)):
                self.state = 7

        elif (self.state == 2):
            if (self.isLetter(char) or self.isDigit(char)):
                self.state = 2
            else:
                self.state = 1
                self.transition(char)
                return "ID"
        
        elif(self.state == 3):
            if (self.isDigit(char)):
                self.state = 3
            else:
                self.state = 1
                self.transition(char)
                return "NUMBER"
        
        elif(self.state == 4):
            self.state = 1
            self.transition(char)
            return "SPECIAL"
        
        elif(self.state == 5):
            if (self.isQuote(char)):
                self.state = 6
            else:
                self.state = 5
        
        elif(self.state == 6):
            self.state = 1
            self.transition(char)
            return "STRING"
            
        elif(self.state == 7):
            if(char == "=" or char == "<" or char == ">"):
                self.state = 8
            else:
                self.state = 1
                self.transition(char)
                return "SPECIAL"
        
        elif(self.state == 8):
            self.state = 1
            self.transition(char)
            return "SPECIAL"


    def isLetter(self, char): 
        return char.isalpha()
        
    def isDigit(self, char):
        return char.isdigit()

    def isSingleSpecial(self, char):
        match = re.match("[\*\+-\/=\(\),]", char)
        if(match):
            return True
        else:
            return False
    
    def isDoubleSpecial(self, char):
        match = re.match("[<>]", char)
        if(match):
            return True
        else:
            return False
    
    def isQuote(self, char):
        return char == "\""
        