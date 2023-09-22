#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # mode = "w" #write (not append), create if doesn't exist
    # myfile = open("textfile.txt", mode)

    # Open the file for appending text to the end
    # mode = "a" # append to existing file, create if doesn't exist
    # myfile = open("textfile.txt", mode)

    # # write some lines of data to the file
    # for i in range(10,15):
    #     mystring = "line "+str(i)+"\n"
    #     myfile.write(mystring)

    # # close the file when done
    # myfile.close

    # Open the file back up and read the contents
    mode = "r" # read
    myfile = open("textfile.txt", mode)
    if myfile.mode == 'r':
        # # read gets entire file
        # contents = myfile.read() # read all
        # print(contents)
        # #for reading, "no need" for closing

        # # readlines() gets a list of all lines into a var
        # fl = myfile.readlines()
        # for x in fl:
        #     print(x)

        # readline() gets one line at a time
        l = myfile.readline()
        print(l)
        l = myfile.readline()
        print(l)

if __name__ == "__main__":
    main()
