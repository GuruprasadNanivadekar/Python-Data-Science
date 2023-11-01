'''
#Even or odd number
def eve(num):
    if num %2==0:
        print("Number is even", num)
    else:
        print("Number is odd", num)

num = int(input('Enter the number'))
eve(num)

#Positive or negative number
def pos(num2):
    if num2 >= 0:
        print("Number is a positive number.")
    else:
        print("Number is a negative number.")
num2 = int(input('Enter the number'))
pos(num2)

#Pass or fail
def grade(marks):
    if marks >= 40:
        print("Congratulations you are pass.")
    else:
        print("Better luck next time")
marks = int(input('Enter your marks'))
grade(marks)

#4
def cat(points):
    if points >= 75:
        print("First class")
    elif points >= 65:
        print("Second class")
    elif score >= 55:
        print("Third class")
    else:
        print("Fail")
points = int(input("Enter your points"))
cat(points)

#Temprature
def temp(temprature):
    if temprature > 40:
        print("It's hot outside.")
    elif 20 <= temprature:
        print("The weather is pleasant.")
    else:
        print("It's cold.")
temprature = int(input("Enter current temprature"))
temp(temprature)
'''