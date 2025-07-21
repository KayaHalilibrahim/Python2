# 1. Create a list named brands with these elements: "Toyota", "Bmw", "Renault", "Mercedes".

cars = ["Toyota", "BMW","Renault", "Mercedes"]

# 2. How many elements are in the list?

lengthOfCars = len(cars)
print(f"Length Of Cars: {lengthOfCars}")

# 3. What is the first and last element of the list?
print(f"First Element: {cars[0]}")
print(f"Last Element: {cars[-1]}")

# 4. Replace "Renault" with "Togg" in the list.

cars [2] ="Togg"
print(cars)

# 5. Is "Togg" in the list?

result = "Togg" in cars
print(result)

# 6. Take the first two elements of the list.

result = cars[0:2]
print(result)

# 7. Add "Ford" and "Citroen" to the end of the list.

cars = cars + ["Ford", "Citroen"]
print (cars)

# 8. Delete the last element of the list.

del cars[-1]    # result = cars.pop(-1)
print (cars)

# 9. Save the following data in a list:
# Student1: Yiğit Bilgi 2010 [70,80,90]
# Student2: Ada Bilgi   2011 [70,70,80]
# Student3: Çınar Turan 2017 [60,60,90]

student1 = ["Yiğit", "Bilgi", 2010, [70, 80, 90]]
student2 = ["Ada", "Bilgi", 2011, [70, 70, 80]]
student3 = ["Çınar", "Turan", 2017, [60, 60, 90]]

students = [student1,student2,student3]

print (student1[3][1])

# 10. Calculate the students’ ages.

print("\n----Ages of students---")

for i in students:
    age = 2025 - i[2]
    print(f"Age of {i[0]}:  {age}")

# 11. Calculate the students’ average grades.

print("\n----Average of students---")

for i in students:
     average = (i[3][0] + i[3][1] + i[3][2])/3
     print(f"Average of {i[0]}: {round(average)}")



"""
Output:
/4.03. ExampleLists.py"
Length Of Cars: 4
First Element: Toyota
Last Element: Mercedes
['Toyota', 'BMW', 'Togg', 'Mercedes']
True
['Toyota', 'BMW']
['Toyota', 'BMW', 'Togg', 'Mercedes', 'Ford', 'Citroen']
['Toyota', 'BMW', 'Togg', 'Mercedes', 'Ford']
80

----Ages of students---
Age of Yiğit:  15
Age of Ada:  14
Age of Çınar:  8

----Average of students---
Average of Yiğit: 80
Average of Ada: 73
Average of Çınar: 70

"""