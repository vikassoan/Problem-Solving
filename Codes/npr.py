def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def npr(n, r):
    permutations = factorial(n) // factorial(n - r)
    return permutations

# Take input from the user
n = int(input("Enter the total number of objects (n): "))
r = int(input("Enter the number of objects to choose (r): "))

# Calculate the number of permutations
result = npr(n, r)

print("Number of permutations (nPr) =", result)
