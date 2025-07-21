programingLanguage = ["Python","C","Java","C#","Javascript"]

result = programingLanguage

result = programingLanguage[0:2]
print(result)


result = programingLanguage[:2]
print(result)

result = programingLanguage[:]
print(result)

result = programingLanguage[-3:-1]
print(result)  # ['Java', 'C#']

result = programingLanguage[-3:]
print(result)

# update

programingLanguage [1] = "PHP"
print(programingLanguage)

result = len(programingLanguage)
print(result)

result = programingLanguage + ["C","Go","Delphi"]
print(result)

result = "Go" in programingLanguage
print (result)

result = "React" in programingLanguage
print (result)

for i,index in enumerate(programingLanguage):
    print(f"{i}. index : {index}")

del programingLanguage[3]
for i in programingLanguage:
    print(i)