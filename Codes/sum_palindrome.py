def is_palindrome(num):
    return str(num) == str(num)[::-1]

def sum_palindrome(num):
    # Reverse the number
    reversed_num = int(str(num)[::-1])
    
    # Add the original number and the reversed number
    total_sum = num + reversed_num
    
    return total_sum

# Take input from the user
num = int(input("Enter a number: "))

# Calculate the sum with its reverse
sum_with_reverse = sum_palindrome(num)

# Check if the sum is a palindrome
if is_palindrome(sum_with_reverse):
    print("The sum of", num, "and its reverse is a palindrome:", sum_with_reverse)
else:
    print("The sum of", num, "and its reverse is not a palindrome:", sum_with_reverse)
