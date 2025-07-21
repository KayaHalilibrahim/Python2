# myList = [1,2,3,4]

# for i in myList:
#     print(i)


for i in range(0,20,2): 
    print(i)


rng = range(10)
result1 = list(rng)
print(result1)

rng2 = range(10,21) # 10-20
result2 = list(rng2)
print(result2)

rng3 = range(100,210,10) 
result3 = list(rng3)
print(result3)

rng4 = range(0,-55,-5) 
result4 = list(rng4)
print(result4)

rng5 = range(20,50,8) 
result5 = list(rng5)
print(result5)


"""
Output:
0
2
4
6
8
10
12
14
16
18
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
[0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]
[20, 28, 36, 44]
"""