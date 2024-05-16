def is_armstrong(num):
    # Convert the number to a string to count the digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Initialize sum
    armstrong_sum = 0
    
    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
