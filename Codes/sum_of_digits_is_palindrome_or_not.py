def is_palindrome(num):
    return str(num) == str(num)[::-1]

def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

# Take input from the user
num = int(input("Enter a number: "))

# Calculate the sum of the digits
sum_of_digits_num = sum_of_digits(num)

# Check if the sum of digits forms a palindrome
if is_palindrome(sum_of_digits_num):
    print("The sum of digits in", num, "forms a palindrome.")
else:
    print("The sum of digits in", num, "does not form a palindrome.")
