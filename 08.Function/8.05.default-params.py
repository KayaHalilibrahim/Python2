def greeting (name = "User",message = "Hello"):
    return f"{message} {name}"


result = greeting("Halil","Hi")
print(result)

result = greeting("İbrahim")
print(result)


result= greeting()
print(result)



def exponentiation(base, exponent = 2):
    return base ** exponent


result = exponentiation(2,3)
print(result)


result = exponentiation(5)
print(result)


def sum (a,b):
    return a+b

def sub(a,b):
    return a-b

def proc(a,b,fn = sum):
    return fn(a,b)


result = proc(10,20,sub)
print(result)


result = proc(10,20,sum)
print(result)

"""
Output:
Hi Halil
Hello İbrahim
Hello User
8
25
-10
30
"""