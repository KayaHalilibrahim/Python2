def sum ():
    return 10+20



result = sum()
print(result)

# print(sum())


def year():
    import datetime
    return datetime.datetime.now().year


def hour():
    import datetime
    return datetime.datetime.now().hour

def calculateAge():
    return year() -1980
    

print(calculateAge())


def greeting():
    if( hour() < 12):
        return "Good Morning"
    else:
        return "Hello"
    

print (greeting())

"""
Output:
30
45
Hello
"""