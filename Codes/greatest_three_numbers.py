def find_greatest(num1, num2, num3):
    greatest = num1
    
    if num2 > greatest:
        greatest = num2
    
    if num3 > greatest:
        greatest = num3
    
    return greatest

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the greatest of the three numbers
result = find_greatest(num1, num2, num3)

print("The greatest of", num1, ",", num2, ", and", num3, "is:", result)
