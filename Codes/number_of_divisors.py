import math

def count_divisors(number):
    # Initialize the count of divisors
    divisor_count = 0
    
    # Iterate from 1 to the square root of the number
    for i in range(1, int(math.sqrt(number)) + 1):
        # If i divides the number evenly
        if number % i == 0:
            # If i is the square root of the number, increment the count by 1
            if i * i == number:
                divisor_count += 1
            # Otherwise, increment the count by 2
            else:
                divisor_count += 2
    
    return divisor_count

# Take input from the user
number = int(input("Enter a positive integer: "))

# Calculate the number of divisors
divisors = count_divisors(number)

print("Number of divisors of", number, ":", divisors)
