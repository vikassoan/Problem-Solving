def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Take input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per year: "))
time = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

print("Simple interest:", simple_interest)
