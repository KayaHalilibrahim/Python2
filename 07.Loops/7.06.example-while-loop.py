# Save the student information entered from the keyboard (n times) into a list.

# The structure of the dictionary list should be: (studentNo, studentName, studentSurname).

# When the adding process is finished, list the students.


students = []  # Empty list to store all student dictionaries

print("To exit the adding process, press 'q'.")

while True:
    i = input("Press any key to continue or 'q' to quit: ")
    if i.lower() == 'q':
        break

    studentNo = input("Enter student no          : ")
    studentName = input("Enter student name        : ")
    studentSurname = input("Enter student surname    : ")

    student = {
        "studentNo": studentNo,
        "studentName": studentName,
        "studentSurname": studentSurname
    }

    students.append(student)  # Add student dictionary to the list

# Print all students
print("\nAll students:")
for s in students:
    print(s)


"""
Output:
To exit the adding process, press 'q'.
Press any key to continue or 'q' to quit: e
Enter student no          : 1
Enter student name        : murat
Enter student surname     : demir
Press any key to continue or 'q' to quit: t
Enter student no          : 2
Enter student name        : mehmet
Enter student surname     : çelik
Press any key to continue or 'q' to quit: q

All students:
{'studentNo': '1', 'studentName': 'murat', 'studentSurname': 'demir'}
{'studentNo': '2', 'studentName': 'mehmet', 'studentSurname': 'çelik'}

"""