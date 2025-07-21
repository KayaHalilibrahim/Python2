# String Concat

name ="Halil"
surname = "Kaya"
age = 22

message1 = "Message1: My name is "+ name + " " + surname + "." + " I am " +str(age) +" years old.\n"
print (message1)



# String Format

message2 = "Message2: My name is {name} {sname}. I am {age} years old\n".format(name=name,sname=surname,age=age)

print(message2)



message3 = "Message3: My name is {} {}. I am {} years old\n".format(name,surname,age)
print(message3)



message4 = "Message4: My name is {0} {1}. I am {2} years old\n".format(name,surname,age)
print(message4)


# f-string
message5 = f"Message5: My name is {name} {surname}. I am {age} years old\n"
print(message5)



"""
Output:
Message1: My name is Halil Kaya. I am 22 years old.

Message2: My name is Halil Kaya. I am 22 years old

Message3: My name is Halil Kaya. I am 22 years old

Message4: My name is Halil Kaya. I am 22 years old

Message5: My name is Halil Kaya. I am 22 years old

"""