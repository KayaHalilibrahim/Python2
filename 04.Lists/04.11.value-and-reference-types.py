# value types

# x = 10
# y = "20"

# x = y

# y = 30

# print(x,y)


# reference types

a = ["apple","banana"]
b = ["apple","pear"]

a = b # address of b equals to address of a.

a[0] = "grape"

print(a,b)



# copy list

listA = [10,20]
listB = listA.copy() # address of listA and listB is diffrent. only value of this list are equal.

# listB = list(listA) another method for copy list.

listB[0] = 30
 
print(listA,listB)