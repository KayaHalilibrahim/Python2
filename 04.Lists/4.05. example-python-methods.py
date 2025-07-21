costumers = ["Halil İbrahim","Mustafa Korkmaz","Mehmet Kaya","Yigit Bilgi"]

orderTotals = [12000,13000,5000,15000]

# 1. Add a 5000 lira order for the user named 'sadikturan'.

orderTotals.append(5000)
print(orderTotals)

# 2. Delete the last added order.

orderTotals.pop()
print(orderTotals)

# 3. For all customers, print this sentence:
# <username> has a total order amount of <amount> liras.
print()
for i,j in zip(costumers,orderTotals):
    print(f"{i} has a total order amount of {j} liras.")

# 4. Sort the customers alphabetically.

print(costumers.sort())

# 5. Sort the order totals from highest to lowest.

orderTotals.reverse()
print(orderTotals)

# 6. Which order is the lowest?

print(f"The lowest orders: {orderTotals[-1]}")

# 7. How many orders does 'sadikturan' have?


# 8. Remove the user 'ahmetyilmaz' from the customers list.

costumers.remove("Yigit Bilgi")
print(costumers)

# 9. Clear all items in both lists.

costumers.clear()
orderTotals.clear()

print(costumers)
print(orderTotals)

# 10. Get a username and order total from the user, and add them to the lists.

name = input("Enter Name: ")
orderPrice = input("Enter Price : ")

costumers.append(name)
orderTotals.append(orderPrice)

print(costumers)
print(orderTotals)


"""
Order:
[12000, 13000, 5000, 15000, 5000]
[12000, 13000, 5000, 15000]

Halil İbrahim has a total order amount of 12000 liras.
Mustafa Korkmaz has a total order amount of 13000 liras.
Mehmet Kaya has a total order amount of 5000 liras.
Yigit Bilgi has a total order amount of 15000 liras.
None
[15000, 5000, 13000, 12000]
The lowest orders: 12000
['Halil İbrahim', 'Mehmet Kaya', 'Mustafa Korkmaz']
[]
[]
Enter Name: Enes
Enter Price : 6000
['Enes']
['6000']
"""