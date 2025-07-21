title = "Programming Lessons with Python"


# 1. How many characters are in the title variable?

pieces = len(title)
print(f"Length of title: {pieces}")
print (title[30])


# 2. Take the first 5 and last 5 characters of the title variable.

firstFive = title[0:5]
print(firstFive)


lastFive = title[pieces-5:]  # title[-5:]
print(lastFive)

# 4. Print the title variable backwards.

backward = title[::-1]
print (backward)
# 5. Print the example sentence based on the student information entered from the keyboard.
# Example: Student Halil Kaya's first grade was calculated as 60 and his second grade as 70.

name = input ("Your Name: ")
surname = input ("Surname: ")
firstGrade = float(input("First Grade: "))
secondGrade = float(input("Second Grade: "))

averageGrade = round(((firstGrade+secondGrade)/2),2)

print(f"Student {name} {surname}'s first grade was calculated as {firstGrade}, his second grade as {secondGrade} and average of grades {averageGrade}.")

"""
Output:
Length of title: 31
n
Progr
ython
nohtyP htiw snosseL gnimmargorP
Your Name: Mustafa
Surname: Kaya
First Grade: 67
Second Grade: 80
Student Mustafa Kaya's first grade was calculated as 67.0, his second grade as 80.0 and average of grades 73.5.
"""