#1. Which one of the two entered numbers is bigger?

number1 = int(input ("Enter Number 1: "))
number2 = int(input ("Enter Number 2: "))


result = (number1 > number2)
print(f"is number1 greater than number2: {result}")

result = (number1 == number2)
print(f"is number1 equals than number2: {result}")

result = (number1 < number2)
print(f"is number1 smaller than number2: {result}")

#2. Check if the entered number is even or odd.

number = int(input ("Enter a Number: "))
result = (number %2 ==0)
print(f"Is number is even: {result}")

#3. Check a student’s success based on 3 entered grades. 50 and above is considered successful.

grade1 = int (input ("Enter grade 1: "))
grade2 = int (input ("Enter grade 2: "))
grade3 = int (input ("Enter grade 3: "))

average = (grade1 + grade2 + grade3) // 3

result = (average >= 50)
print(f"Is student successful: {result}")

