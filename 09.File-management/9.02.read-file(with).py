# file = open ("log.txt",encoding="utf-8")
# # utf-8 to read Turkish characters correctly.

# print(file.read())

# file.close()


"with : After the process is completed, the file is automatically closed."


with open ("log.txt",encoding="utf-8") as myFile:
    print(myFile.read(10)) # read 10 characters
    print(myFile.tell())   # show position of cursor. (11)
    print(myFile.read())  
    print(myFile.tell())  # 72
    
    myFile.seek(0)
    for i in myFile:  # prints line by line.
        print(i)



      

"""
end="" --> delete space line.
with end:
Halil İbrahim Kaya
Bandırma Onyedi Eylül Üniversitesi
Cyber Security
"""

"""
without end:
Halil İbrahim Kaya

Bandırma Onyedi Eylül Üniversitesi

Cyber Security
"""


"""
Output:
Halil İbra
11
him Kaya
Bandırma Onyedi Eylül Üniversitesi
Cyber Security
72
Halil İbrahim Kaya

Bandırma Onyedi Eylül Üniversitesi

Cyber Security
"""