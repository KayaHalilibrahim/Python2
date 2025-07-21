products = [
    {"productName": "Hp Victus", "price": 32999},
    {"productName": "Lenovo ThinkPad", "price": 25499},
    {"productName": "Apple Macbook", "price": 49999},
    {"productName": "Huawei Matebook", "price": 26999},
    {"productName": "Casper Nirvana", "price": 20000}
]



# 1. Apply the example sentence below for all products:
#     "The price of the Hp Victus is 32999 Turkish Lira."

for product in products:
    print(f"The price of the {product['productName']} is {product['price']} Turkish Lira.")


# 2. What is the total of all product prices?

totalPrice = 0
for i in products:
    totalPrice += i["price"]

print (f"Total of products price: {totalPrice}")


# 3. List the products whose price is between 25000 and 40000.


print()

for i in products:
    price = i["price"]
    if price >=25000 and price <= 40000:
        print(f'{i["productName"]} : {price}')


# 4. Ask the user to enter a keyword. List the products that include that keyword.

print ()

keyword = input("Enter a key: ")

for i in products:
    if keyword.lower() in i["productName"].lower():
        print(f"{i['productName']} : {i['price']}")


"""
Output:
The price of the Hp Victus is 32999 Turkish Lira.
The price of the Lenovo ThinkPad is 25499 Turkish Lira.
The price of the Apple Macbook is 49999 Turkish Lira.
The price of the Huawei Matebook is 26999 Turkish Lira.
The price of the Casper Nirvana is 20000 Turkish Lira.
Total of products price: 155496

Hp Victus : 32999
Lenovo ThinkPad : 25499
Huawei Matebook : 26999

Enter a key: H
Hp Victus : 32999
Lenovo ThinkPad : 25499
Huawei Matebook : 26999
"""