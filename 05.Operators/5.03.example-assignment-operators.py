a, b, c = 4, 8, (12, 2)


#1. What is the difference between the product of two numbers entered by the user and the sum of a, b, and c?

total = a+b+c[0]+c[1]

number1 = int (input("Enter number1: "))
number2 = int (input("Enter number2: "))
mulOfNumbers = number1*number2

result = mulOfNumbers - total
print(result) 

# 2. Calculate the result of c divided by b without remainder (integer division).

result = sum(c) // b
print(result)

print()

#3. What is the result of (a + b + c) modulo 7?

result = (a + b + sum(c)) % 7
print(result)

#4. Calculate b to the power of a.

result = b**a
print(result)

#5. Given the unpacking a, *b, c = (2, 4, 6, 8, 13), what is the cube of c?

a, *b, c = (2, 4, 6, 8, 13)  # b = 4, 6, 8
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

result = c ** 3
print(result)

#6. Given the unpacking a, b, *c = (2, 4, 6, 8, 13), what is the total (sum) of the values in c?

a, b, *c = (2, 4, 6, 8, 13) # 6, 8, 13
result = sum(c)
print(c)


"""
Output:
Enter number1: 10
Enter number2: 5
24
1

5
4096
a: 2
b: [4, 6, 8]
c: 13
2197
[6, 8, 13]
"""