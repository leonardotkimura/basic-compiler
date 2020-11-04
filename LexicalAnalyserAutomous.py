class LexicalAnalyserAutomous:
    def __init__(self):
        self.state = 1

    def transition(self, char):
        if (self.state == 1):
            if (self.isLetter(char)):
                self.state = 2

        if (self.state == 2):
            if (self.isLetter(char) or self.isDigit(char)):
                self.state = 2
            else:
                self.state = 1
                self.transition(char)
                return "ID"

    def isLetter(self, char): 
        return char.isalpha()
        

    def isDigit(self, char):
        return char.isdigit()

        