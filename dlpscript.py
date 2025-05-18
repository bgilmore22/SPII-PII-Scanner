from dlpScannerExt import scan_file  #We first import the main function from the other file
import sys  #THis import is needed to access command line arguments

#The main function then runs when the script gets executed by a user
def main():
    #We first check if a file path was given by the user in the command line arguments
    if len(sys.argv) < 2:
        print("Usage: python dlpscript.py <file_path>")
        return

    #We then extract the file path from the command line argument given by the user
    file_path = sys.argv[1]

    #We then run the scan on the user's given file
    scan_file(file_path)

if __name__ == "__main__":
    main()


