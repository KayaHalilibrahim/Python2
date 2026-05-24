courseName = "Halil ile Python Programlama Dersleri."
website = "https://halilibrahimkaya.net"

# 1. Remove any spaces from the beginning and end of the string "Halil"

result = courseName.strip()

# 2. Convert all characters in the variable 'courseName' to lowercase letters

result = courseName.lower()
print(result)


# 3. Count how many times the dot character '.' appears in the variable 'website'
result = website.count('.')
print(result)

# 4. Check if the 'website' variable starts with "https"
result = website.startswith('https') # True
print(result)

# 5. Check if the 'website' variable ends with "tr"
result = website.endswith('tr') # False
print(result)

# 6. Check if all characters in 'courseName' are only letters (no spaces or symbols)

result = website.isalpha() # False
print(result)

# 7. Replace all space characters in 'courseName' with dashes '-'

result = courseName.replace(' ','-')
print(result)

# 8. Replace the word "Python" in 'courseName' with "ReactJs"

result = courseName.replace("Python", 'ReactJs')
print(result)

# 9. Check if the 'website' variable contains the substring "www"

result = courseName.find('www')  # -1 
print(result)

# 10. Convert the string 'courseName' into a list of characters
result = courseName.split()
print(result)


"""
Output:
halil ile python programlama dersleri.
1
True
False
False
Halil-ile-Python-Programlama-Dersleri.
Halil ile ReactJs Programlama Dersleri.
-1
['Halil', 'ile', 'Python', 'Programlama', 'Dersleri.']

"""
