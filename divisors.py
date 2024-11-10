import sys

# Get the number from the command line argument
number = int(sys.argv[1])

# Loop through all numbers from 1 to 'number'
for i in range(1, number + 1):
    if number % i == 0:  # Check if the remainder is 0
        print(i, end=" ")

print()
