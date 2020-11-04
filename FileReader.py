class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def execute(self):
        fo = open(self.fileName, "r+")
        print ("Name of the file: ", fo.name)

        Lines = fo.readlines() 
        formattedLines = []
        count = 0

        for line in Lines: 
            formattedLines.append(line)

        fo.close()

        return formattedLines