"""
Tuple & List
Tuple cannot be changed, list can be changed. Tuple uses ( ), list uses \[ ]. Tuple is faster and good for fixed data, list is used for adding or removing items.
"""


myList = [1,2,3,4]

myTuple = 6,7,8,6,5,7   # myTuple = (1,2,3)  

print(type(myList))
print(type(myTuple))

myList[2]=10

result = myList[2]
print(result)

#myTuple[2]=10 --> we can no change it.
 
result = myTuple[0]  
print(result)


result = myTuple.count(7)
print(result)

result = myTuple.index(5) # give index of 5.
print(result)


myTuple2 = tuple(myList)
print(type(myTuple2))

myList2 = list(myTuple2)
print(type(myList2))

"""
Output:
<class 'list'>
<class 'tuple'>
10
6
2
4
<class 'tuple'>
<class 'list'>
"""