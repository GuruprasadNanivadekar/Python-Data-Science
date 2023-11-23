
def add_numbers(a, b):
    return a + b

# Example using positional arguments
result_1 = add_numbers(5, 3)
result_2 = add_numbers(-1, 10)
print("Positional Arguments:")
print(f"5 + 3 = {result_1}")
print(f"-1 + 10 = {result_2}")


# Function with keyword arguments
def greet_person(name, message):
    return f"Hello, {name}! {message}"

# Example using keyword arguments
greeting_1 = greet_person(name="Guru", message="Nice to meet you!")
greeting_2 = greet_person(message="How was your day?", name="Ravi")
print("\nKeyword Arguments:")
print(greeting_1)
print(greeting_2)

# Function with default arguments
def power(base, exponent=2):
    return base ** exponent

# Example using default arguments
result_3 = power(3)
result_4 = power(2, 4)
print("\nDefault Arguments:")
print(f"3^2 = {result_3}")
print(f"2^4 = {result_4}")
# Function with variable-length arguments
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example using variable-length arguments
result_5 = sum_values(1, 2, 3)
result_6 = sum_values(5, 10, 15, 20)
print("\nVariable-Length Arguments:")
print(f"Sum of 1, 2, 3 = {result_5}")
print(f"Sum of 5, 10, 15, 20 = {result_6}")
