class ExpAutonomous:
    def __init__(self):
        self.state = 1
        self.expCodeGenerator = None
        self.codeLines = []
    
    def transition(token):
        # grandes transições
        return 0

    def raiseException(self, token):
        raise Exception("invalid Transition on state: {}; token: {}".format(self.state, token.value))

        
    def instantiateExpAutomousIfNot(self):
        if(self.expAutonomous == None):
            self.expAutonomous = ExpAutonomous()

    def reset(self):
        self.state = 1