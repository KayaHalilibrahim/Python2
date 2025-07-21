institution = "BTK Academy".split () # str to list

print (type (institution))
print (institution)

print(institution[0])
print(institution[1])


numbers = [1,2,3,4,5]
names = ["Mustfa","Enes","Ayşe"]

print(type(numbers))
print(type(numbers[0]))


print(type(names))
print(type(names[0]))


student1 = ["Halil","Kaya",70,80,90]
print(student1[0] + " "+student1[1])


average =(student1[2] + student1[3] +student1[4]) /3
print(average)


students = [["Murat","Durmaz",80,70,90], ["Mehmet","kormaz",80,90,90]]
print(students[1])
print(students[0][1])
    

"""
Output:
<class 'list'>
['BTK', 'Academy']
BTK
Academy
<class 'list'>
<class 'int'>
<class 'list'>
<class 'str'>
Halil Kaya
80.0
['Mehmet', 'kormaz', 80, 90, 90]
Durmaz
"""