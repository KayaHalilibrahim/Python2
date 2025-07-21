import math

""" 
1. Calculate the area and circumference of a circle with a given radius.

2. Calculate the km information entered from the keyboard in miles. mile = km 7 1.609344

"""

# 1

r = float (input ("Please enter radius: "))

area = math.pi * (r**2)          # pow (r,2)
circumference = 2* math.pi * r

print(f"Area: {area} \nCircumference: {circumference}")


# 2 

km = input("Please enter km: ")
km = float(km)

# mile = km / 1.609344

mile = round ((km / 1.609344),2) # Takes 2 digits after the decimal point.

print (f"Mile: {mile}")
