def reverse_digits(num):
    # Convert the number to a string and reverse it
    num_str = str(num)
    reversed_num_str = num_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num_str)
    
    return reversed_num

# Take input from the user
num = int(input("Enter a number: "))

# Call the function to reverse the digits
reversed_num = reverse_digits(num)

print("Original number:", num)
print("Reversed number:", reversed_num)
