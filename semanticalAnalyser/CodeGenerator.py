class CodeGenerator:
    def __init__(self):
        self.codeLines = []
        return None
    
    def addCodeLines(self, codeLines):
        self.codeLines = codeLines
    
    def printCode(self):
        for codeLine in self.codeLines:
            print(codeLine)
