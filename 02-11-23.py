'''
Question 1:
•	Positional arguments are passed to a function in a specific order, and the function uses the order of the arguments to determine their values.
•	Keyword arguments allows to pass arguments to a function by specifying the parameter names along with their values
•	Default arguments are parameters with predefined values. If the caller of the function doesn't provide a value for a default argument, the default value is used.
•	*args allows a function to accept any number of positional arguments. **kwargs allows a function to accept any number of keyword arguments.
Question 2:
•	Positional Arguments:
Positional arguments are passed to a function in a specific order, and their values are determined by their position in the argument list.
The function expects the arguments in a particular sequence, and changing the order of arguments can change their meaning.
•	Keyword Arguments:
Keyword arguments are passed to a function by explicitly specifying the parameter names along with their values, regardless of the order.
They are particularly useful when you want to provide values for only a subset of the function's parameters, and you don't have to worry about the order of the parameters.
Question 3:
•	*Args:
The *args syntax allows a function to accept any number of positional arguments. These arguments are collected into a tuple within the function.
It returns output in tuple format.

•	**kwargs:
The **kwargs syntax allows a function to accept any number of keyword arguments. These arguments are collected into a dictionary within the function.
It returns output in dictionary format.
Question 4:
*args (Positional Variable-Length Arguments):
*args is used to pass a variable number of positional arguments to a function. The asterisk (*) before "args" collects any additional positional arguments into a tuple, which can be accessed within the function.
It is often used when you want to create a function that can accept an arbitrary number of arguments without knowing in advance how many there will be.
**kwargs (Keyword Variable-Length Arguments):
•	**kwargs is used to pass a variable number of keyword arguments to a function. The double asterisk (**) before "kwargs" collects any additional keyword arguments into a dictionary, where the keys are the parameter names and the values are the corresponding argument values.
•	It is useful when you want to create a function that can accept a variety of named parameters without knowing all the possible parameter names beforehand.

'''

# *args Examples:

def sum(*args):
    result = 0
    for num in args:
        result += num
    return result

total = sum(1, 2, 3, 4, 5)
print(total)
print('-----------------------------------------------------')

def string(*args):
    result = ""
    for string in args:
        result += string
    return result

combined = string("Hello, ", "World!", " How are you?")
print(combined)
print('-----------------------------------------------------')

# **kwargs Example:
def create(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

info = create(name="Guru", age=24, city="Pune")
print(info)
print('-----------------------------------------------------')

def pet(**kwargs):
    p = {}
    for key, value in kwargs.items():
        p[key] = value
    return p

details = pet(category="Dog", breed="Labrador", birth=2022, color="Black")
print(details)


