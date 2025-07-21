# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Y can not be zero")

# except ValueError:
#     print("x and y must be number.")

# except:
#     print("Bilinmeyen bir hata oluştu.")


# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("There should be x and y number. Also can't be y 0")
#     print(e)  # can be saved to the file.To examine later
# except:
#     print("Bilinmeyen bir hata oluştu.")




# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except Exception as e:
#     print("Bilinmeyen bir hata oluştu.")
#     print(e)
# else:        # It works if it does not enter the except block.
#     print("Everything is fine,No error.")
        

# while True:
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x/y)
#     except Exception as e:
#         print("Bilinmeyen bir hata oluştu.")
#         print(e)
#     else:     
#         break


while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as e:
        print("Bilinmeyen bir hata oluştu.")
        print(e)
    else:
        break
    finally:  # It works in all situations. For example, it can be used to close an opened file.
        print("The finally block worked.")


"""
Output:
x: 10
y: 0
Bilinmeyen bir hata oluştu.
division by zero
The finally block worked.
x: 20
y: 15v
Bilinmeyen bir hata oluştu.
invalid literal for int() with base 10: '15v'
The finally block worked.
x: 50
y: 10
5.0
The finally block worked.
"""