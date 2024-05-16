def generate_ap_series(a, d, n):
    ap_series = [a + (i - 1) * d for i in range(1, n + 1)]
    return ap_series

# Take input from the user
first_term = int(input("Enter the first term of the AP: "))
common_difference = int(input("Enter the common difference of the AP: "))
n = int(input("Enter the value of n (nth term): "))

# Generate the AP series
ap_series = generate_ap_series(first_term, common_difference, n)

# Print the AP series
print("Arithmetic Progression (AP) series up to nth term:")
print(ap_series)
