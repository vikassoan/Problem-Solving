def nth_term_of_series(n):
    nth_term = (n * (n + 1)) // 2
    return nth_term

# Take input from the user
n = int(input("Enter the value of n: "))

# Calculate the nth term of the series
result = nth_term_of_series(n)

print("The", n, "th term of the series is:", result)
