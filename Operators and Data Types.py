age = 15
print(type(age))
print("Age:", age)

weight = 45.5
print(type(weight))
print("Weight:", weight)

name = "Codingal"
print(type(name))
print("Name:", name)

is_student = True
print(type(is_student))
print("Is Student:", is_student)

print("\n")

age1 = float(age)
print("Age as float:", age1)
print(type(age1))

weight = int(weight)
print("Weight as int:", weight)
print(type(weight))

print("\n")


# arithmetic operations
x = 12
y = 15

print("Addition:", x + y)
print("Subtraction:", y - x)
print("Multiplication:", x * y)
print("Division:", y / x)
print("Floor Division:", y // x)
print("Modulus:", y % x)
print("Exponentiation:", x ** y)

print("\n")

# comparison operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print("\n")

# string operations
string = "Codingal"
print(len(string))
print(string[0])
print(string[2:5])  # slicing

# number swap
a = 12
b = 6
temp = a
a = b
b = temp
print("After swapping: a =",a, ", b =", b)
