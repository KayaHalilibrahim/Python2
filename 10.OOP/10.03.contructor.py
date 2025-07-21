# Class 

class Product:
    pass
    #attribute, propert

    def __init__(self,name,isActive,price = 20000):
        self.name = name
        self.price = price
        self.isActive = isActive
    
    #method
    


# Instance, Object
p1 = Product("Samsung A51",False,15000)
p2 = Product("Iphone 15",True,50000)
p3 = Product("Redmi 10",True)

print(p1.name)
print(p1.isActive)
print()

print(p2.name)
print(p2.price)
print()


products = [p1, p2, p3]

for product in products:
    print(f"Product name: {product.name}      - Price:{product.price}")


"""
Output:
Samsung A51
False

Iphone 15
50000

Product name: Samsung A51      - Price:15000
Product name: Iphone 15      - Price:50000
Product name: Redmi 10      - Price:20000
"""