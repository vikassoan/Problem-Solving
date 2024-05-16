def moving_average(stream):
    total_sum = 0
    count = 0
    
    for i, num in enumerate(stream, start=1):
        total_sum += num
        count += 1
        average = total_sum / count
        print("{:.2f}".format(average), end=" ")
    print()

# Example input
arr = [10, 20, 30, 40, 50]

# Calculate and print the moving average
print("Moving average:")
moving_average(arr)
