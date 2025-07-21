# 1- Write a function that prints a given word a given number of times on the screen.

def rewrite(name):
    for i in range(n):
        print(name)

n = 5

rewrite("Halil")



# 2- Write a function that calculates the area and perimeter of a rectangle.

shortEdge = 5
longEdge = 12

def area(shortEdge,longEdge):
    return shortEdge*longEdge

def perimeter(shortEdge,longEdge):
    return 2*(shortEdge+longEdge)


print(f"Area of rectangle: {area(shortEdge,longEdge)}")
print(f"perimeter of rectangle: {perimeter(shortEdge,longEdge)}")


# 3- Create a coin toss (heads or tails) application using a function. (Use the random module)

print()

def headTails():
    import random
    number = random.random()

    if (number >= 0.5):
        return "Head"
    else:
        return "Tail"

result = headTails()
print(result)
# 4- Write a function that finds all prime numbers between two given numbers.


print()

def findPrimeNumbers(number1, number2):
    for number in range(number1,number2):
        if(number > 1):
            for i in range(2,number):
                if(number % i == 0):
                    break
            else:                   # to 'for'
                print(number)

                

findPrimeNumbers(10,20)

# 5- Write a function that returns all divisors of a given number as a list

def divisor (number):
    perfectDivisors = []

    for i in range (2,number):
        if (number % i == 0):
            perfectDivisors.append(i)

    
    return perfectDivisors


print(divisor(20))


"""
Output:
Halil
Halil
Halil
Halil
Halil
Area of rectangle: 60
perimeter of rectangle: 34

Tail

11
13
17
19
[2, 4, 5, 10]
"""