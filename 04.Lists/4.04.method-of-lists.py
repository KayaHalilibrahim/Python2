numbers = [4,50,60,4,20,5,60]
names = ["Ahmet","Muhammed","Zeynep","Ali"]

result = min(numbers)
print (result)

result = min(names)
print (result)

result = max(numbers)
print (result)

result = max(names)
print (result)


# Adding
numbers.append(75)
print(numbers)


names.append("İbrahim")
print(names)

names.insert(2,"Mustafa")
print(names)

names.insert(-1,"Hasan")
print(names)

numbers.insert(-3,63)
print(numbers)

# Deleting 

numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

names.pop(5)
print(names)


names.remove("İbrahim")
print(names)

numbers.remove(20)
print(numbers)



# Sorting

numbers.sort()
print(numbers)

names.sort()
print(names)


numbers.reverse()
print(numbers)

names.reverse()
print(names)


# Search

result = names.count("Muhammed")
print(result)

result = numbers.count(4)
print(result)


result = numbers.index(4)
print(result)

result = names.index("Ali")
print(result)



"""
Output:
4
Ahmet
60
Zeynep
[4, 50, 60, 4, 20, 5, 60, 75]
['Ahmet', 'Muhammed', 'Zeynep', 'Ali', 'İbrahim']
['Ahmet', 'Muhammed', 'Mustafa', 'Zeynep', 'Ali', 'İbrahim']
['Ahmet', 'Muhammed', 'Mustafa', 'Zeynep', 'Ali', 'Hasan', 'İbrahim']
[4, 50, 60, 4, 20, 63, 5, 60, 75]
[4, 50, 60, 4, 20, 63, 5, 60]
[4, 50, 4, 20, 63, 5, 60]
['Ahmet', 'Muhammed', 'Mustafa', 'Zeynep', 'Ali', 'İbrahim']
['Ahmet', 'Muhammed', 'Mustafa', 'Zeynep', 'Ali']
[4, 50, 4, 63, 5, 60]
[4, 4, 5, 50, 60, 63]
['Ahmet', 'Ali', 'Muhammed', 'Mustafa', 'Zeynep']
[63, 60, 50, 5, 4, 4]
['Zeynep', 'Mustafa', 'Muhammed', 'Ali', 'Ahmet']
1
2
4
3
"""