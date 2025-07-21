name = "Halil İbrahim"

for i in name:
    if (i =="i"):
        continue
    print(i)

print ("\n-----\n")

for i in name:
    if (i =="i"):
        break
    print(i)


print ("\n-----\n")

i = 0
while (i < 5 ):
    i +=1
    if(i == 2):
        continue
    print(i)

print()

i = 0
while (i < 5 ):
    i +=1
    if(i == 2):
        break
    print(i)



"""
Output:
H
a
l
l
 
İ
b
r
a
h
m

-----

H
a
l

-----

1
3
4
5

1

"""