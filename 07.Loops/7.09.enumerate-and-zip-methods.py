# Enumerate

brands = ["TOGG","BMW","MERCEDES","FORD"]

# index = 1
# for brand in brands:
#     print(f"{index}-{brand}")
#     index +=1


# obj1 = enumerate(brands)
# print(type(obj1))
# print(list(obj1))


obj1 = enumerate(brands,1) # 1 is start value
print(type(obj1))
print(list(obj1))


for index,brand in enumerate(brands,1):
    print(f"{index}-{brand}")


# Zip
print("\n------ZIP------\n")

numbers = [100,200,300]
students = ["Ali","Ömer","Zeynep"]

print (list(zip(numbers,students)))

print()

for no,name in zip(numbers,students):
    print(f"{no} : {name}")

