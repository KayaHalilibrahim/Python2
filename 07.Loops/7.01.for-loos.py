# for --> list

numbers = [1,20,15,6,8,40,30]
name = "Halil İbrahim Kaya"


for i in numbers:
    print (i)


for i in numbers:
    print ("Hello world")


for c in name:
    print(c)

print()

myTuple = [(1,2),(3,4),(5,6)]

for a,b in myTuple:
    print(a,b)


print()

myDict = {"63":"Şanlıurfa",
          "34":"İstanbul",
          "6":"Ankara",
          "10":"Balıkesir"}

for x in myDict:
    print(myDict[x])

print()
for x in myDict.values():
    print(x)


print()
for x in myDict.keys():
    print(x)


print()
for x in myDict.items():
    print(x)


"""
Output:
1
20
15
6
8
40
30
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
Hello world
H
a
l
i
l
 
İ
b
r
a
h
i
m
 
K
a
y
a

1 2
3 4
5 6

Şanlıurfa
İstanbul
Ankara
Balıkesir

Şanlıurfa
İstanbul
Ankara
Balıkesir

63
34
6
10

('63', 'Şanlıurfa')
('34', 'İstanbul')
('6', 'Ankara')
('10', 'Balıkesir')
"""