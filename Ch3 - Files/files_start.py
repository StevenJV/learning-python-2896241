#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # mode = "w" #write (not append), create if doesn't exist
    # myfile = open("textfile.txt", mode)

    # Open the file for appending text to the end
    mode = "a" # append to existing file, create if doesn't exist
    myfile = open("textfile.txt", mode)

    # write some lines of data to the file
    for i in range(10,15):
        mystring = "line "+str(i)+"\n"
        myfile.write(mystring)

    # close the file when done
    myfile.close

    # Open the file back up and read the contents


if __name__ == "__main__":
    main()
