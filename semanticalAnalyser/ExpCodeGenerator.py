from .ExpAutonomous import ExpAutonomous
from .Stack import Stack

class ExpCodeGenerator:
    def __init__(self):
        self.elementStack = Stack()
        self.operatorStack = Stack()
        self.expAutonomous = ExpAutonomous()
        self.codeLines = []
        self.temporaryCounter = 0
    
    def transition(self, token):
        action = self.expAutonomous.transition(token)
        print("token: {} , state: {} ".format(token.value, self.expAutonomous.state))
        print("action:{} ".format(action))

        # colocar os códigos de cada ação
        if (action=="ACTION_A"):
            self.elementStack.push(token.value)

        elif (action=="ACTION_B"):
            self.elementStack.push(token.value)

        elif (action=="ACTION_C"):
            self.operatorStack.push(token.value)

        elif (action=="ACTION_E"):
            while (self.operatorStack.peek() != "("):
                operator = self.operatorStack.pop()
                self.generateCode(operator)
            self.operatorStack.pop()

        elif (action=="ACTION_F"):
            while (self.operatorStack.peek() in ["+","-","*","/"]):
                operator = self.operatorStack.pop()
                self.generateCode(operator)
            self.operatorStack.push("+")

        elif (action=="ACTION_G"):
            while (self.operatorStack.peek() in ["+","-","*","/"]):
                operator = self.operatorStack.pop()
                self.generateCode(operator)
            self.operatorStack.push("-")

        elif (action=="ACTION_H"):
            while (self.operatorStack.peek() in ["*","/"]):
                operator = self.operatorStack.pop()
                self.generateCode(operator)
            self.operatorStack.push("*")
        
        elif (action=="ACTION_I"):
            while (self.operatorStack.peek() in ["*","/"]):
                operator = self.operatorStack.pop()
                self.generateCode(operator)
            self.operatorStack.push("/")
        
        elif (action=="ACTION_J"):
            print("starting action J")
            while(not self.operatorStack.isEmpty()):
                print(self.elementStack)
                print(self.operatorStack)
                operator = self.operatorStack.pop()
                if( operator in ["+","-","*","/"]):
                    self.generateCode(operator)
            return True # accepted

        

        return 0

    def generateCode(self, operator):
        elementB = self.elementStack.pop()
        elementA = self.elementStack.pop()

        self.codeLines.append("mov     rax,[{}]".format(elementA))
        if(operator == "+"):
            self.codeLines.append("add     rax,[{}]".format(elementB))
        elif(operator == "-"):
            self.codeLines.append("sub     rax,[{}]".format(elementB))
        # elif(operator == "*"):
            # self.codeLines.append("mov      r9,[{}]".format(elementB))
            # self.codeLines.append("mul     r9")
        # elif(operator == "/"):
            # self.codeLines.append("add     rax,[{}]".format(elementB))

        temporaryVariable = "temp{}".format(self.temporaryCounter)
        self.temporaryCounter += 1
        self.codeLines.append("mov     [{}], rax".format(temporaryVariable))
        self.elementStack.push(temporaryVariable)

    def getCodeLines(self):
        return self.codeLines

    def raiseException(self, token):
        raise Exception("invalid Transition on state: {}; token: {}".format(self.state, token.value))

    def reset(self):
        self.state = 1
        self.codeLines = []