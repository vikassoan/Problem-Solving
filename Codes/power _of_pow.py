def sum_of_squares_of_evens(n):
    # Initialize the sum
    total_sum = 0
    
    # Iterate over even numbers from 2 to n
    for i in range(2, n+1, 2):
        # Add the square of the current even number to the sum
        total_sum += i**2
    
    return total_sum

# Take input from the user
n = int(input("Enter a number: "))

# Calculate the sum of squares of even numbers up to n
result = sum_of_squares_of_evens(n)

print("Sum of squares of even numbers up to", n, ":", result)
