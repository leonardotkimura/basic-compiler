from .ExpAutonomous import ExpAutonomous

class ExpCodeGenerator:
    def __init__(self):
        self.stack = None
        self.expAutonomous = ExpAutonomous()
    
    def generateCode(token):
        action = self.expAutonomous.transition(token)

        # colocar os códigos de cada ação

        return 0



    def raiseException(self, token):
        raise Exception("invalid Transition on state: {}; token: {}".format(self.state, token.value))

    def reset(self):
        self.state = 1