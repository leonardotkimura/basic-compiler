from FileReader import FileReader
from lexicalAnalyser.LexicalAnalyser import LexicalAnalyser

import sys

def main(argv):
    fileReader = FileReader(argv[1])
    lexicalAnalyser = LexicalAnalyser()
    
    text = fileReader.execute()
    
    tokens = lexicalAnalyser.execute(text)
    for token in tokens:
        print(token.type, token.value)

if __name__ == "__main__":
    main(sys.argv)
