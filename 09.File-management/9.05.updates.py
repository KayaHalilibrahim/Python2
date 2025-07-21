# with  open("brands.txt","a") as file:
#     file.write("2-Open\n")
#     file.write("4-Mazda\n")
#     file.write("5-Mercedes\n")
#     file .write("6-BMW\n")

# with open ("brands.txt","r+",encoding="utf-8") as file:
#     brands = file.read()
#     brands = "1-Toyota\n" + brands
#     file.seek(0)
#     file.write(brands)

# with open("brands.txt","r+",encoding="utf-8") as file:
#     brands = file.readlines()
#     brands.insert(2,"3- Renault\n")
#     file.seek(0)
#     for brand in brands:
#         file.write(brand)
    

with open("brands.txt",encoding="utf-8") as file:
    print(file.read())


with open("brands.txt","r+",encoding="utf-8") as file:
    myBrandList = file.readlines()
    myBrandList.insert(0,"0- Ford\n")
    file.seek(0)
    file.writelines(myBrandList)


with open("brands.txt",encoding="utf-8") as file:
    print(file.read())


"""
Output:

1- Toyota
2- Opel
3- Renault
4- Mazda
5- Mercedes
6- BMW
0- Ford
1- Toyota
2- Opel
3- Renault
4- Mazda
5- Mercedes
6- BMW

"""