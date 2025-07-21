import datetime 

def greeting(name):
    return f"Hello {name}"


def sum (number1,number2):
    return number1+number2

def calculateAge(year):
    now = datetime.datetime.now().year
    return now - year

def pension(birthYear,name):
    age = calculateAge(birthYear) 
    remainingTime = 65 - age
    if (remainingTime > 0):
        return f"{name}, you have {remainingTime} years left until retirement."
    else:
        return f"{name},you have already been retired for {abs(remainingTime)} years."

print(greeting("Halil"))
print(greeting("İbrahim"))


print()
print(sum(10,20))
print(sum(50,60))


print()
print(calculateAge(1986))

print()

print(pension(1980,"Mustafa"))
print(pension(1955,"Mustafa"))

"""
Output:
Hello Halil
Hello İbrahim

30
110

39

Mustafa, you have 20 years left until retirement.
Mustafa,you have already been retired for 5 years.
"""