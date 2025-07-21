x = [2,4,6]
y = [2,4,6]

z = y

# identity
print (x == y)  # value of x and y are equals
print(x is y)   #  Object x and object y is not same.
print(x is not y)   #  True

print()
print(z is y)   #  Object z and object y is  same.
print(z is not y)

# membership
print("\nMembership example")
print(10 in x)
print(10 not in  x)


"""
Output:
True
False
True

True
False

Membership example
False
True
"""