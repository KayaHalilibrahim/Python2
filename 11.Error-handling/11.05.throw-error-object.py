# print(10 / 0)

x = 10

# if x > 5:
#     raise ValueError ("X cannot be greater than 5. ")


def colorIt (text,color):
    colors = ("blue","red","yellow","orange")
    if type(text) is not str:
        raise TypeError("Text should be of string type.")
    
    if type(color) is not str:
        raise TypeError("Color should be of string type.")

    if color not in colors:
        raise ValueError("invalid color")
    
    print(f"{text} was written as {color}.")


try:
    colorIt ("Thanks","black")
    colorIt ("Good Morning","red")
    colorIt ("Wellcome","blue")
except (TypeError,ValueError) as e:
    print(e)
