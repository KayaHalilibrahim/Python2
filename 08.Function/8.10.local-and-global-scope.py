# local scope


# global scope


# x = "global scope"

# def myFunc():
#     x = "local scope"
#     print(x)


# myFunc()    #local scope
# print(x)    #global scope


# name = "Mustafa"


# def changeName (newName):
#     global name
#     name = newName
#     print(name)


# changeName("Ayşe")  #Ayşe
# print(name)         #Ayşe

# name = "Global String"
# def greeting():
#     # name = "Ali"


#     def hello():
#         # name = "Mustafa"
#         print("Hello ",name)

    
#     hello()

# greeting()


x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"Changed x to {x}")


test()
print(x)