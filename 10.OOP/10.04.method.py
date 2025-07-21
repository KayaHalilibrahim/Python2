# Class 

class Product:
    pass
    #attribute, propert

    def __init__(self,name,isActive,price):
        self.name = name
        self.price = price
        self.isActive = isActive
    
    # Instance method
    def getProduct(self):
        return f"Product name: {self.name}     - Price:{self.kdvPrice()}"

    def kdvPrice (self):
        return self.price *1.20
    


# Instance, Object
p1 = Product("Samsung A51",False,15000)


result = p1.getProduct()
print(result)

result = p1.kdvPrice()
print(result)

"""
Output:
Product name: Samsung A51     - Price:18000.0
18000.0
"""