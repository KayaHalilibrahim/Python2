import module # import module as m


result = module.number
print(result)


result = module.numbers
print(result)

result = module.product
print(result)


result = module.product["productName"]
print(result)

result = module.product["colors"][1]
print(result)


result = module.sum(63,20)
print(result)


print("*************")

from module import number,numbers,product,sum # from module import *

print(number)
print(product)
print(sum(20,30))


"""
Output:
20
[1, 2, 3, 4]
{'productName': 'Iphone 150', 'price': 6000, 'colors': ['blue', 'brown']}
Iphone 150
brown
83
*************
20
{'productName': 'Iphone 150', 'price': 6000, 'colors': ['blue', 'brown']}
50
"""