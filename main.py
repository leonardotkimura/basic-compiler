from FileReader import FileReader
from lexicalAnalyser.LexicalAnalyser import LexicalAnalyser
from syntaticalAnalyser.SyntaticalAnalyser import SyntaticalAnalyser

import sys

def main(argv):
    fileReader = FileReader(argv[1])
    lexicalAnalyser = LexicalAnalyser()
    syntaticalAnalyser = SyntaticalAnalyser()
    
    text = fileReader.execute()
    
    tokens = lexicalAnalyser.execute(text)
    for token in tokens:
        print(token.type, token.value)

    print("\n\nStarting analyser")
    syntaticalAnalyser.recognize(tokens)
    print("\nprogram accepted")

if __name__ == "__main__":
    main(sys.argv)
