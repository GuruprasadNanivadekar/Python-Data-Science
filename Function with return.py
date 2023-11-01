'''
#1
def ad(a, b):
    result = a + b
    return result

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
sum_result = ad(num1, num2)
print("The sum is:", sum_result)


#2
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number"))
factorial = fact(num)
print("The factorial of is:",factorial)

#3
def oddeve(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number"))
if oddeve(num):
    print("Given nuber is even.",num)
else:
    print("Given number is odd.",num)


#4
def F(a, b, c):
    return max(a, b, c)

# Example usage
maximum = F(8, 12, 5)
print(maximum)  # This will print 12

'''
#5
def squ(number):
    return number * number

# Example usage
result = squ(7)
print(result)  # This will print 49
