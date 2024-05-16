def dice_probability(target_number, sides=6):
    # Ensure the target number is within the valid range
    if target_number < 1 or target_number > sides:
        return "Invalid target number"
    
    # Calculate the probability of rolling the target number
    probability = 1 / sides
    
    return probability

# Take input from the user for the target number
target = int(input("Enter the target number you want to roll: "))

# Calculate the probability of rolling the target number
probability = dice_probability(target)

print("Probability of rolling a", target, "with a single fair six-sided die:", probability)
