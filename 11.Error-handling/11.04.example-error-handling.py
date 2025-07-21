theList = ["1", "3", "5", "20b", "abc", "10a", "60"]

# 1. Find the numeric values in the list. Ignore the ones that are not numbers.

for number in theList:
    try:
        int(number)
        print(number)
    except:
        pass

# 2. Ask the user to enter a value. Keep asking until the user writes 'quit' or 'q'. Make sure the input is a number. If not, show an error message.
# print("Enter the number.To exit, press' q.")

print()

while True:
    try:
        number = input("Enter Number: ")
        int(number)           
    except Exception as e:
        print(e)
    finally:
        if(number == "q"):
            print("It is getting out of the application.")
            break
    


# 3. Write a function called get(dict, key) that takes a dictionary and a key. If the key exists, return its value. If not, return None.

# urun = {"urunAdi": "samsung s10"}

# d["fiyat"]             => KeyError
# get(urun, "fiyat")     => None
# get(urun, "urunAdi")   => samsung s10

print()

def get(dict,key):
    try:
        return dict[key] 
    except KeyError:
        return None


product = {"productName":"Samsung A51"}


result = get(product,"price")
print(result)

result = get(product,"productName")
print(result)



"""
Output:
1
3
5
60

Enter Number: q
invalid literal for int() with base 10: 'q'
It is getting out of the application.

None
Samsung A51
"""