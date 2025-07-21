# def displayUser(*args):
#     print(type(args))
#     print(args)


# displayUser()


"""
<class 'tuple'>
()
"""


def displayUser(**kwargs):
    # print(type(kwargs)) 
    # print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print()

"""
<class 'dict'>
{}
"""

displayUser(username="Halilibrahim")
displayUser(username="Halilibrahim",email ="halilibrahim@gmail.com")
displayUser(username="Halilibrahim",email ="halilibrahim@gmail.com",country = "Turkey")
 

def myFunc(a,b,c, *args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


myFunc(10,20,30,40,50,60,key1="value",key2="value2")



"""
Output:
username : Halilibrahim

username : Halilibrahim
email : halilibrahim@gmail.com

username : Halilibrahim
email : halilibrahim@gmail.com
country : Turkey

10
20
30
(40, 50, 60)
{'key1': 'value', 'key2': 'value2'}
"""