from FileReader import FileReader
import sys

def main(argv):
    fileReader = FileReader(argv[1])
    lines = fileReader.execute()

    print(lines)

if __name__ == "__main__":
    main(sys.argv)
