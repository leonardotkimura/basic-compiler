from .SyntaticalAnalyserAutomous import SyntaticalAnalyserAutomous

class SyntaticalAnalyser:
    def __init__(self):
        self.automous = SyntaticalAnalyserAutomous()
        self.tokens = []

    def recognize(self, tokens):

        for token in tokens:
            # transition the automous. If error, will raise an error
            self.automous.transition(token)
            print("token: {} , state: {} ".format(token.value, self.automous.state))

        return True