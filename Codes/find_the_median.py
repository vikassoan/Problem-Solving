def find_median(arr):
    arr.sort()  # Sort the array
    n = len(arr)
    if n % 2 == 0:  # If the length of the array is even
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:  # If the length of the array is odd
        median = arr[n//2]
    return median

# Take input array from the user
arr = []
n = int(input("Enter the number of elements in the array: "))
print("Enter the elements of the array:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Call the function to find the median
median = find_median(arr)
print("Median of the array:", median)
