from .ExpAutonomous import ExpAutonomous

class SyntaticalAnalyserAutomous:
    def __init__(self):
        self.state = 1
        self.expAutonomous = ExpAutonomous()

    def transition(self, token):

################## Program States #######################
        if (self.state == 1):
            if (token.type == "NUMBER"):
                self.state = 2
            else:
                self.raiseException()

        elif (self.state == 2):
            if (token.type == "ID" and token.value == "LET"):
                self.state = 5
            elif (token.type == "END"):
                self.state = 4
            else:
                self.raiseException()
        
        elif (self.state == 3):
            if (token.type == "NUMBER"):
                self.state = 2
            else:
                self.raiseException()
        
        # End State
        elif (self.state == 4):  
            self.raiseException()
        

################## "LET" States #######################
        elif (self.state == 5):
            if (token.type == "VAR"):
                self.state = 6
            else:
                self.raiseException()
        
        elif (self.state == 6):
            if (token.type == "SPECIAL" and token.value == "="):
                self.state = 7
            else:
                self.raiseException()

        elif (self.state == 7):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 8
                self.transition(token)

        # empty Transition
        elif (self.state == 8):
            self.state = 3
            self.transition(token)

    def raiseException(self):
        print("raise Exception")
        print(self.state)
        