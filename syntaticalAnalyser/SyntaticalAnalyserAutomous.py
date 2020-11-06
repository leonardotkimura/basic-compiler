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
                self.raiseException(token)

        elif (self.state == 2):
            if (token.type == "ID" and token.value == "LET"):
                self.state = 5
            elif (token.type == "ID" and token.value == "READ"):
                self.state = 9
            elif (token.type == "ID" and token.value == "DATA"):
                self.state = 11
            elif (token.type == "ID" and token.value == "PRINT"):
                self.state = 13
            elif (token.type == "ID" and token.value == "GO"):
                self.state = 15
            elif (token.type == "ID" and token.value == "GOTO"):
                self.state = 16
            elif (token.type == "ID" and token.value == "IF"):
                self.state = 18
            elif (token.type == "ID" and token.value == "FOR"):
                self.state = 24
            elif (token.type == "ID" and token.value == "NEXT"):
                self.state = 33
            elif (token.type == "ID" and token.value == "GOSUB"):
                self.state = 36
            elif (token.type == "ID" and token.value == "RETURN"):
                self.state = 38
            elif (token.type == "END"):
                self.state = 4
            else:
                self.raiseException(token)
        
        elif (self.state == 3):
            if (token.type == "NUMBER"):
                self.state = 2
            else:
                self.raiseException(token)
        
        # End State
        elif (self.state == 4):  
            self.raiseException(token)
        

################## "LET" States #######################
        elif (self.state == 5):
            if (token.type == "VAR"):
                self.state = 6
            else:
                self.raiseException(token)
        
        elif (self.state == 6):
            if (token.type == "SPECIAL" and token.value == "="):
                self.state = 7
            else:
                self.raiseException(token)

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

################## "READ" States #######################
        elif (self.state == 9):
            if (token.type == "VAR"):
                self.state = 10
            else:
                self.raiseException(token)
        
        elif (self.state == 10):
            if (token.type == "SPECIAL" and token.value == ","):
                self.state = 9
            else:
                self.state = 3
                self.transition(token)

################## "DATA" States #######################
        elif (self.state == 11):
            if (token.type == "NUMBER"):
                self.state = 12
            else:
                self.raiseException(token)
        
        elif (self.state == 12):
            if (token.type == "SPECIAL" and token.value == ","):
                self.state = 11
            else:
                self.state = 3
                self.transition(token)

################## "PRINT" States #######################
        elif (self.state == 13):
            if (token.type == "STRING" or token.type == "VAR"):
                self.state = 14
            else:
                self.raiseException(token)
        
        elif (self.state == 14):
            if (token.type == "SPECIAL" and token.value == ","):
                self.state = 13
            else:
                self.state = 3
                self.transition(token)

################## "GOTO" States #######################
        elif (self.state == 15):
            if (token.type == "ID" and token.value == "TO"):
                self.state = 16
            else:
                self.raiseException(token)
        
        elif (self.state == 16):
            if (token.type == "NUMBER"):
                self.state = 17
            else:
                self.raiseException(token)

        elif (self.state == 17):
            self.state = 3
            self.transition(token)

################## "IF" States #######################
        elif (self.state == 18):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 19
                self.transition(token)
        
        elif (self.state == 19):
            if (token.type == "SPECIAL" and (token.value in [">","<","=","<>",">=","<="])):
                self.state = 20
            else:
                self.raiseException(token)

        elif (self.state == 20):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 21
                self.transition(token)
        
        elif (self.state == 21):
            if (token.type == "ID" and token.value == "THEN"):
                self.state = 22
            else:
                self.raiseException(token)
        
        elif (self.state == 22):
            if (token.type == "NUMBER"):
                self.state = 23
            else:
                self.raiseException(token)

        elif (self.state == 23):
            self.state = 3
            self.transition(token)

################## "For" States #######################
        elif (self.state == 24):
            if (token.type == "LETTER"):
                self.state = 25
            elif (token.type == "VAR"):
                self.state = 25
            else:
                self.raiseException(token)
        
        elif (self.state == 25):
            if (token.type == "SPECIAL" and (token.value == "=")):
                self.state = 27
            else:
                self.raiseException(token)

        elif (self.state == 27):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 28
                self.transition(token)
        
        elif (self.state == 28):
            if (token.type == "ID" and token.value == "TO"):
                self.state = 29
            else:
                self.raiseException(token)
        
        elif (self.state == 29):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 30
                self.transition(token)

        # End state
        elif (self.state == 30):
            if (token.type == "ID" and token.value == "STEP"):
                self.state = 31
            else:
                self.state = 3
                self.transition(token)
        
        elif (self.state == 31):
            accept = self.expAutonomous.transition(token)
            if (accept):
                self.expAutonomous.reset()
                self.state = 32
                self.transition(token)
        
        # End state
        elif (self.state == 32):
            self.state = 3
            self.transition(token)

################## "NEXT" States #######################
        elif (self.state == 33):
            if (token.type == "LETTER"):
                self.state = 34
            elif (token.type == "VAR"):
                self.state = 34
            else:
                self.raiseException(token)
       
        # End state
        elif (self.state == 34):
            self.state = 3
            self.transition(token)

################## "GOSUB" States #######################
        elif (self.state == 36):
            if (token.type == "NUMBER"):
                self.state = 37
            else:
                self.raiseException(token)
       
        # End state
        elif (self.state == 37):
            self.state = 3
            self.transition(token)

################## "RETURN" States #######################
        # End state
        elif (self.state == 38):
            self.state = 3
            self.transition(token)
    
    
    def raiseException(self, token):
        raise Exception("invalid Transition on state: {}; token: {}".format(self.state, token.value))
        