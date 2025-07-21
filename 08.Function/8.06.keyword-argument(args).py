
def fullName (firstName:str,lastName:str)-> str: # We want the parameters and return value to be str.
    return f"Your name: {firstName} {lastName}"


result = fullName("Halil İbrahim","Kaya")
print(result)


result = fullName(lastName="Kaya",firstName="Halil")
print(result)


result = fullName(lastName=10,firstName="Halil")
print(result)


result = fullName(firstName="Murat",lastName="Korkmaz")
print(result)

"""
Output:
Your name: Halil İbrahim Kaya
Your name: Halil Kaya
Your name: Halil 10
Your name: Murat Korkmaz
"""