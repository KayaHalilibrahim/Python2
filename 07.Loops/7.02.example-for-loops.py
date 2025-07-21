numbers = [3, 5, 7, 2, 12, 32, 45]
products = ["samsung s24", "samsung s22", "iphone 15", "iphone 14"]

# For the list numbers:

#1. Print each element in the list.

for i in numbers:
    print (i)

print()


#2. Find which numbers in the list are divisible by 3.

for i in numbers:
    if (i %3 == 0):
        print(i)

print()

#3. Find the total (sum) of all numbers in the list.

total = 0
for i in numbers:
    total += i
print(f"Total of nuumbers: {total}")

print()




# For the list products:

#4. List all products that are iPhone.

for i in products:
    if "iphone" in i:
        print(i)


#5. How many Samsung products are there in the list?

print()
count = 0

for i in products:
    if "samsung" in i:
        count += 1

print(f"Number of Samsung: {count}")
        

"""
Output:
3
5
7
2
12
32
45

3
12
45

Total of nuumbers: 106

iphone 15
iphone 14

Number of Samsung: 2
"""