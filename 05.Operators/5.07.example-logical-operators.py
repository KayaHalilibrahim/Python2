#1.Check if the person is allowed to work: age must be over 18 or have parental permission.

age = int(input("Enter age: "))
parentPermission = True

result = (age > 18) or (parentPermission ==True)
print(f"He can work: {result}")

#2. If the course grade is between 50 and 100, print "Passed"; otherwise, print "Failed".

averageGrade = int(input("Enter Average Grade: "))
result = (averageGrade >=50 ) or (averageGrade <100)

print(f"Passed: {result}")

#3. If the average grade is at least 70 and there is no weak subject, check if the student can get a certificate of appreciation.

averageGrade = 75
weakSubject = False

result = (averageGrade > 70) and (weakSubject != True)
print(f"This Studentcan get a certificate of appreciation {result}")
 

#4. To get a job, check if the person has at least an associate or bachelor's degree. Also check if they don’t smoke.

associateDegree = False 
bachelorDegree = True
smoke = True

result = ((associateDegree) or (associateDegree)) and (smoke)
print(f"get a jop: {result}")


#5. Do login control for the app using "username and "password".

uname = "Halil"
passw = "123456"

username = input("Enter username: ")
password = input("Enter password: ")
result = (username == uname) and (passw == password)
print(f"You can log in: {result}")

"""
Output:
Enter age: 19
He can work: True
Enter Average Grade: 75
Passed: True
This Studentcan get a certificate of appreciation True
get a jop: False
Enter username: Halil
Enter password: 123456
You can log in: True
"""