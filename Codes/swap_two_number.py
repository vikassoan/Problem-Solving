# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
