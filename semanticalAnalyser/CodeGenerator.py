class CodeGenerator:
    def __init__(self):
        self.defBottlerplate()
        self.codeLines = []
        return None
    
    def addCodeLines(self, codeLines):
        self.codeLines = codeLines
    
    def printCode(self):
        for codeLine in self.codeLines:
            print(codeLine)
    
    def writeFile(self, filename):
        file = open(filename, "w")
        for line in self.header:
            file.write(line)
            file.write("\n")
        for line in self.codeLines:
            file.write(line)
            file.write("\n")
        for line in self.footer:
            file.write(line)
            file.write("\n")
        file.close()

    def defBottlerplate(self):
        self.header = [
            "section     .text",
            "global      _start                              ;must be declared for linker (ld)",
            "_start:"
        ]

        self.footer = [
            "_end:",
            "int     0x80                                ;call kernel",
            "section     .data",
            "temp0       dd  0",
            "temp1       dd  0",
            "temp2       dd  0",
            "temp3       dd  0",
            "temp4       dd  0",
            "temp5       dd  0",
            "temp6       dd  0",
            "temp7       dd  0",
            "temp8       dd  0",
            "temp9       dd  0",

            "A           dd  100",
            "B           dd  50",
            "C           dd  20",
        ]