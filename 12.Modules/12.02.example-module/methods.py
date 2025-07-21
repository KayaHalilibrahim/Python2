from db import products

def addProduct(name,price,color):
    products.append({
        "name":name,
        "price":price,
        "color":color
    })
    print("Product added.\n")

    

def updateProduct(id,name,price):
    products[id-1].update({
        "name":name,
        "price":price
    })
    print("Product updated.\n")


def showProducts():
    for i in products:
        print(f"Product name: {i['name']}\nProduct price: {i['price']}\nProduct color: {i['color']}\n")




