# Class 

class Product:
    pass
    #method
    #attribute, propert


# Instance, Object
product1 = Product()
product2 = Product()



result = type(product1)
print(result)

result = type (product2)
print(result)

result = product1  # <__main__.Product object at 0x7fd836fb5bd0> adress of object
print(result)

result = product2  # 0x7f528cab1c50
print(result)


"""
Output:
<class '__main__.Product'>
<class '__main__.Product'>
<__main__.Product object at 0x7f528cab1950>
<__main__.Product object at 0x7f528cab1c50>
"""