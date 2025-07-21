# "w" :Write mode
# ** create file current location
# ** If the same file exists in the location, it deletes the file and creates a new file.

"""
file = open("file.txt","w",encoding="utf-8")

file.write("Hasan Kaya\n")
file.write("Zeynep Kaya\n")


file.close()
"""


with open("file.txt","w") as myFile:  # no need close method.
    myFile.write("Halil İbrahim Kaya\n")
    myFile.write("Hasan Kaya\n")


with open("file.txt") as readFile:
    print(readFile.read())