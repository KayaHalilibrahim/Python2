# Help was received.


# Function to enter student name and notes
def enter_note():
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    note1 = input("Note 1: ")
    note2 = input("Note 2: ")
    note3 = input("Note 3: ")

    # Save the notes in a text file
    with open("exam_notes.txt", "a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + note1 + ',' + note2 + ',' + note3 + '\n')
    print("Notes saved.\n")


# Function to calculate average and letter grade
def calculate_grade(line):
    line = line.strip()  # remove newline character
    parts = line.split(":")  # split name and notes
    student_name = parts[0]
    notes = parts[1].split(",")  # split 3 notes

    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])
    average = (note1 + note2 + note3) / 3

    # Determine the letter grade
    if average >= 90:
        grade = "AA"
    elif average >= 85:
        grade = "BA"
    elif average >= 80:
        grade = "BB"
    elif average >= 75:
        grade = "CB"
    elif average >= 70:
        grade = "CC"
    elif average >= 65:
        grade = "DC"
    elif average >= 60:
        grade = "DD"
    elif average >= 50:
        grade = "FD"
    else:
        grade = "FF"

    return f"{student_name} --> {average:.2f} --> {grade}"


# Function to read and show all notes
def show_notes():
    with open("exam_notes.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


# MENU
while True:
    print("\n1 - Enter Note")
    print("2 - Show Notes with Average and Grade")
    print("3 - Exit")

    choice = input("Select an option: ")

    if choice == "1":
        enter_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")


"""
Output:
1 - Enter Note
2 - Show Notes with Average and Grade
3 - Exit
Select an option: 1
Enter student name: Ali 
Enter student surname: Kaya
Note 1: 80
Note 2: 85
Note 3: 90
Notes saved.


1 - Enter Note
2 - Show Notes with Average and Grade
3 - Exit
Select an option: 2
Ayşe Demir --> 76.67 --> CB
Ali Kaya --> 85.00 --> BA

1 - Enter Note
2 - Show Notes with Average and Grade
3 - Exit
"""