
class ExpAutonomous:
    def __init__(self):
        self.state = 1
        self.expAutonomous = None
        self.codeLines = []
    
    def transition(self, token):

################## Program States #######################
        if (self.state == 1):
            if (token.type == "VAR" or token.type == "LETTER"):
                self.state = 4
                return "ACTION_A"
            elif (token.type == "NUMBER"):
                self.state = 4
                return "ACTION_B"
            elif (token.type == "SPECIAL" and token.value == "("):
                self.state = 2
                return "ACTION_C"
            else:
                self.raiseException(token)

        elif (self.state == 2):
            self.instantiateExpAutonomousIfNot()
            action = self.expAutonomous.transition(token)
            if (action == "ACTION_J"):
                self.state = 4 
                self.expAutonomous.reset()
                return "ACTION_D"
            else:
                return action
        
        elif (self.state == 3):
            if (token.type == "SPECIAL" and token.value == ")"):
                self.state = 4
                return "ACTION_E"
            else:
                self.raiseException(token)
        
        # End State
        elif (self.state == 4):  
            if (token.type == "SPECIAL" and token.value == "+"):
                self.state = 1
                return "ACTION_F"
            elif (token.type == "SPECIAL" and token.value == "-"):
                self.state = 1
                return "ACTION_G"
            elif (token.type == "SPECIAL" and token.value == "*"):
                self.state = 1
                return "ACTION_H"
            elif (token.type == "SPECIAL" and token.value == "/"):
                self.state = 1
                return "ACTION_I"
            else:
                return "ACTION_J"  # "Accepted"


    def raiseException(self, token):
        raise Exception("invalid Transition on state: {}; token: {}".format(self.state, token.value))

        
    def instantiateExpAutonomousIfNot(self):
        if(self.expAutonomous == None):
            self.expAutonomous = ExpAutonomous()

    def reset(self):
        self.state = 1