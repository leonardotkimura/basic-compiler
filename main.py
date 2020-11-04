from FileReader import FileReader
from LexicalAnalyser import LexicalAnalyser

import sys

def main(argv):
    fileReader = FileReader(argv[1])
    lexicalAnalyser = LexicalAnalyser()
    
    lines = fileReader.execute()
    print(lines)
    tokens = lexicalAnalyser.execute(lines)
    for token in tokens:
        print(token.type, token.value)

if __name__ == "__main__":
    main(sys.argv)
