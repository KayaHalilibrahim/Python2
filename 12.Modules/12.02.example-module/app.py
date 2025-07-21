from methods import showProducts,addProduct,updateProduct

# print("Enter product information")
# productName = input("Product name: ")
# productPrice = int(input("Product price: "))
# productColor = input("Product color: ")

addProduct("Redmi 10",15000,"Green")
updateProduct(2,"Samsung A51",30000)
showProducts()


"""
Output:
Product added.

Product updated.

Product name: Samsung S24
Product price: 20000
Product color: Black

Product name: Samsung A51
Product price: 30000
Product color: White

Product name: Redmi 10
Product price: 15000
Product color: Green
"""