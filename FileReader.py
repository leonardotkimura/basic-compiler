class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def execute(self):
        fo = open(self.fileName, "r+")
        print ("Name of the file: ", fo.name)

        text = fo.read()
        return text