""""
To open or create a file, we use the open() method.

Usage           :open(filename, accessMode)
accessMode      :Tells what we want to do with the file.
"r"             :Read mode. The file must already exist.
seek            :Moves the cursor to a position in the file.

"""

f = open("log.txt")




print(f.read())
print(f.read()) # gives space

f.seek(0)
print(f.read())
print(f.read())


f.seek(19)
print(f.read())
print()

f.seek(0)
print(f.readline())


f.seek(0)
lines = f.readlines()
print(lines)

isClosed = f.closed  # not method it is a attribute.
print(isClosed)

f.close()
isClosed = f.closed  
print(isClosed)


""""
Output:
Halil İbrahim Kaya
Bandırma Onyedi Eylül Üniversitesi
Cyber Security

Halil İbrahim Kaya
Bandırma Onyedi Eylül Üniversitesi
Cyber Security


Bandırma Onyedi Eylül Üniversitesi
Cyber Security

Halil İbrahim Kaya

['Halil İbrahim Kaya\n', 'Bandırma Onyedi Eylül Üniversitesi\n', 'Cyber Security']
False
True
"""