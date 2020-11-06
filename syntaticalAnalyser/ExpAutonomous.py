class ExpAutonomous:
    def __init__(self):
        self.state = 1
        self.expAutonomous = None

    def transition(self, token):

################## Program States #######################
        if (self.state == 1):
            if (token.type == "NUMBER"):
                self.state = 4
            elif (token.type == "ID"): # change to VAR
                self.state = 4
            elif (token.type == "SPECIAL" and token.value == "("):
                self.state = 2
            elif (token.type == "ID" and token.value == "SEN"): # change to predef
                self.state = 6
            elif (token.type == "ID" and token.value == "FN"):
                self.state = 5
            else:
                self.raiseException()

        elif (self.state == 2):
            self.instantiateExpAutomousIfNot()
            accepted = self.expAutonomous.transition(token)
            if (accepted):
                self.expAutonomous.reset()
                self.state = 3
                self.transition(token)
        
        elif (self.state == 3):
            if (token.type == "SPECIAL" and token.value == ")"):
                self.state = 4
            else:
                self.raiseException()
        
        # End State
        elif (self.state == 4):  
            if (token.type == "SPECIAL" and (token.value == "+" or 
                                             token.value == "-" or 
                                             token.value == "*" or 
                                             token.value == "/")):
                self.state = 1
            else:
                return True  # "Accepted"
        
        elif (self.state == 5):
            if (token.type == "ID"): # CHANGE TO LETTER
                self.state = 6
            else:
                self.raiseException()

        elif (self.state == 6):
            if (token.type == "SPECIAL" and token.value == "("):
                self.state = 2
            else:
                self.raiseException()

    def raiseException(self):
        print("raise Exception")
        
    def instantiateExpAutomousIfNot(self):
        if(self.expAutonomous == None):
            self.expAutonomous = ExpAutonomous()

    def reset(self):
        self.state = 1