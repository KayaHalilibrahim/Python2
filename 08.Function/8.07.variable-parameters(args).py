# def sum(a,b):
#     return a + b

def sum(*args):
    print(args)
    print(type(args))
    result = 0
    for i in args:
        result +=i
    
    return result

result = sum (10,20)
result = sum (10,20,30)
result = sum (10,20,30,40)


print(result)


"""
Output:
(10, 20)
<class 'tuple'>
(10, 20, 30)
<class 'tuple'>
(10, 20, 30, 40)
<class 'tuple'>
100
"""