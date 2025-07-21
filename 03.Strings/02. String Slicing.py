course = "Python Programming"

print(course[0])         # Prints the first character:
print(course[-1])        # Prints the last character

piece = len(course)      # Total number of characters in the string

print(piece)             # Prints 18

print(course[piece - 1]) # Prints the last character

print(course[0:5])       # Takes characters from index 0 to 4 
print(course[:6])        # Takes characters from start to index 5 

print(course[7:19])      # Takes characters from index 7 to 18 
print(course[7:piece])   # Same as above; from index 7 to end 

print(course[7:])        # From index 7 to end 

print(course[-11:-1])    # From 11th-last to 2nd-last character 
print(course[-11:])      # From 11th-last to end 

print(course[0:19:2])    # From index 0 to 18, step 2 
print(course[::])        # Whole string (default slicing) 

print(course[::-1])      # Reverses the string 


"""
Output:

P
g
18
g
Pytho
Python
Programming
Programming
Programming
Programmin
Programming
Pto rgamn
Python Programming
gnimmargorP nohtyP

"""

