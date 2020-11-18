from FileReader import FileReader
from lexicalAnalyser.LexicalAnalyser import LexicalAnalyser
from syntaticalAnalyser.SyntaticalAnalyser import SyntaticalAnalyser
from semanticalAnalyser.SemanticalAnalyser import SemanticalAnalyser

import sys

def main(argv):
    fileReader = FileReader(argv[1])
    lexicalAnalyser = LexicalAnalyser()
    syntaticalAnalyser = SyntaticalAnalyser()
    semanticalAnalyser = SemanticalAnalyser()
    
    text = fileReader.execute()
    
    tokens = lexicalAnalyser.execute(text)
    for token in tokens:
        print(token.type, token.value)

    # print("\n\nStarting analyser")
    # syntaticalAnalyser.recognize(tokens)
    # print("\nprogram accepted")

    semanticalAnalyser.generateCode(tokens)

if __name__ == "__main__":
    main(sys.argv)
