x = 9

result = (x>5) and (x<10)
print(result)

#1.and
# True, True --> True

result = (x > 0 ) or (x%2 == 0) # x is even
print(result)

#2. or
# True, True --> True
# True, False --> True
# False, False --> False

#3. NOT
# True -->False
# False -->True

result = not(x > 0)
print(result)