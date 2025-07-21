# 1. Ask the user for a start and end number.
# Then print all even numbers between these two numbers.

startNumber = int (input("Enter the star number: "))
endnumber = int (input("Enter the end number: "))
 
i = startNumber

while (i <= endnumber):

    if (i % 2 ==0):
        print(i)
    i+=1

# 2. Print the numbers from 10 to 1 in reverse order.

print()

k = 10
while (k >=1):
    print(k)
    k-=1

# 3. Ask the user to enter 5 numbers.
# Then print these numbers in sorted order.

j = 0
numbers = []
while (j < 5):
    number = int (input("Enter number: "))
    numbers.append(number)
    j += 1

numbers.sort()
print(numbers)

# 4. Ask the user to enter a username.
# If the input is empty or just spaces, keep asking again until a valid username is entered.

result = True
username = input ("Enter username without space: ")
while (True):
    if (" " in username):
        username = input ("Again! Enter username without space: ")
    else:
        print("Good.")
        break

"""
Output:
Enter the star number: 10
Enter the end number: 19
10
12
14
16
18

10
9
8
7
6
5
4
3
2
1
Enter number: 20
Enter number: 10
Enter number: 30
Enter number: 7 
Enter number: 15
[7, 10, 15, 20, 30]
Enter username without space: dfsdsdf 
Again! Enter username without space: dsfsdf 
Again! Enter username without space: fsdfds
Good.
"""