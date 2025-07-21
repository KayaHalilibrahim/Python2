# 1- Create a factorial function and provide error messages for invalid input values.

def factorial (number):
    x = int(number)
    if (x < 0):
        raise ValueError("Negative Value")
    
    result = 1
    for i in range(1,x+1):
        result *= i
    
    return result



for i in [5,3,'2a',-5]:
    try:
        x = factorial(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)




# 2- Provide an error message if the entered password contains Turkish characters.


password = input("Enter password: ")

turkishChars = "çğıöşüÇĞİÖŞÜ"
try:
    for char in password:
        if char in turkishChars:
            raise ValueError("The password must not contain Turkish characters.")

except Exception as e:
    print (e)

else:
    print(f"Your password: {password}")



"""
Output:
120
6
invalid literal for int() with base 10: '2a'
Negative Value
Enter password: abcçdef
The password must not contain Turkish characters.
"""