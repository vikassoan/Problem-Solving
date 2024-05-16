def multiplication_table(number, length):
    print("Multiplication table for", number, ":")
    for i in range(1, length + 1):
        print(number, "x", i, "=", number * i)

# Take input from the user
num = int(input("Enter a number to generate its multiplication table: "))
table_length = int(input("Enter the length of the multiplication table: "))

# Generate the multiplication table
multiplication_table(num, table_length)
