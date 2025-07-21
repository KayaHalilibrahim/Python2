# Save the following student information in a dictionary:

#  101 → Yiğit Bilgi, born in 2010, grades: (40, 80, 90)

#  102 → Ada Bilgi, born in 2012, grades: (80, 80, 80)

#  103 → Çınar Turan, born in 2017, grades: (70, 70, 70)

# Ask the user to enter a student number. Then print:

# "Student number 101 is Yiğit Bilgi. Age is 14 and average grade is 70."


students = {
    101: {
        "name": "Yiğit Bilgi",
        "birth_year": 2010,
        "grades": [40, 80, 90]
    },
    102: {
        "name": "Ada Bilgi",
        "birth_year": 2012,
        "grades": [80, 80, 80]
    },
    103: {
        "name": "Çınar Turan",
        "birth_year": 2017,
        "grades": [70, 70, 70]
    }
}

number = int(input("Enter student number: "))
student = students[number]
average = sum(student["grades"]) / len(student["grades"])
age = 2025 - student["birth_year"]

print(f"Student number {number} is {student['name']}. Age is {age} and average grade is {average}.")


"""
Output:
Please enter the number of student(101,102 or 103): 101
70.0
Student number 101 is Yiğit Bilgi. Age is 15 and average grade is 70.0
"""





