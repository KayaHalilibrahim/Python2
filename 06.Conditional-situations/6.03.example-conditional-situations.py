# Fuel Cost Calculation

# Write a program that asks the user for the fuel type (gasoline, diesel, or lpg) and the distance.
# Then calculate how much money is needed for that trip.

# Fuel prices:
#     gasoline: 39.35
#     diesel: 41.71
#     lpg: 20.28

distance = float(input("Enter distance in km: "))
fuelType = input("Enter the type of fuel (gasoline, diesel, lpg): ").lower()

if fuelType == "gasoline":
    print(f"Price of fuel: {distance * 39.35}")

elif fuelType == "diesel":
    print(f"Price of fuel: {distance * 41.71}")

elif fuelType == "lpg":
    print(f"Price of fuel: {distance * 20.28}")

else:
    print("Invalid fuel type.")


# Student Grade Evaluation
# Ask the user to enter 2 written exam grades and 1 oral exam grade.
# Calculate the average score.
# Then, print the grade level based on this average:

exam1 = int(input("Enter first exam grade: "))
exam2 = int(input("Enter second exam grade: "))
quiz = int(input("Enter quiz grade: "))

average = (exam1 + exam2 + quiz) / 3

if average >= 0 and average <= 24:
    print("Your grade is 0")

elif average <= 44:
    print("Your grade is 1")
    
elif average <= 54:
    print("Your grade is 2")

elif average <= 69:
    print("Your grade is 3")

elif average <= 84:
    print("Your grade is 4")

elif average <= 100:
    print("Your grade is 5")

else:
    print("Invalid grade average.")


#     If average is between 0 and 24 → grade is 0
#     If average is between 25 and 44 → grade is 1
#     If average is between 45 and 54 → grade is 2
#     If average is between 55 and 69 → grade is 3
#     If average is between 70 and 84 → grade is 4
#     If average is between 85 and 100 → grade is 5

""""
Output:
Enter distance in km: 50
Enter the type of fuel (gasoline, diesel, lpg): diesel
Price of fuel: 2085.5
Enter first exam grade: 60
Enter second exam grade: 90
Enter quiz grade: 100
Your grade is 4

"""