# open(file_name, access_mode)
# access_mode → tells how we want to open the file.

# "r": (Read) mode. Gives error if the file does not exist.
# "w": (Write) mode.
#      ** Creates the file if it doesn't exist.
#      ** Deletes the old content and writes new.
# "a": (Append) mode. Adds to the end. Creates the file if it doesn’t exist.
# "r+": Read and write mode. Gives error if the file does not exist.


# with open("file.txt","a") as myFile:
#     myFile.write("First Line\n")

#     myFile.seek(0)              #We cannot move the cursor in "a" mode.
#     myFile.write("Second Line\n")


"""
    Halil İbrahim Kaya
Hasan Kaya
First Line
First Line
First Line
Second LineFirst Line
Second Line
    """


with open("file.txt","r+") as myFile:
    # myFile.seek(0)
    myFile.write("Fourth Line\n")


""""
Output:
Fourth Line
an Kaya

First Line
Second Line
First Line
Second Line
First Line
Second Line

"""