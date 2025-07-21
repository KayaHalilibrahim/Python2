#       Sets
# cannot be indexed.
# cannot be sorted.
# cannot be updated.
# cannot be repeated.
# We can add and delete elements.

fruits = {"apple","pear","cherry","apple"}
fruits2 = {"apple","pear","cherry","melon"}

result = fruits
print(result)

fruits


for i in fruits:
    print(i)


print()

result = "apple" in fruits
print(result)


fruits.add("watermelon")
print(fruits)


fruits.update(fruits2)
print(fruits)


fruits.remove("apple")   # If there is no this element, it throws an error.
print(fruits)

fruits.discard("pear") # No error.
print(fruits)


fruits.pop() # random deleting
print(fruits)



