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
            if (self.isSpecial(char)):
                self.state = 4
            if (self.isQuote(char)):
                self.state = 5

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
            if (self.isSpecial(char)):
                self.state = 4
            else:
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
                


    def isLetter(self, char): 
        return char.isalpha()
        
    def isDigit(self, char):
        return char.isdigit()

    def isSpecial(self, char):
        match = re.match("[\*\+-\/<>=\(\),]", char)
        if(match):
            return True
        else:
            return False
    
    def isQuote(self, char):
        return char == "\""
        