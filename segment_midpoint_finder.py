# Segment Midpoint Finder
# Written by Sean-e
# v1 on Friday, October 2nd, 2026

# Collect user input
x1 = input('Enter the x of your first set of coordinates: ')
y1 = input('Enter the y of your first set of coordinates: ')
x2 = input('Enter the x of your second set of coordinates: ')
y2 = input('Enter the y of your second set of coordinates: ')

# Make our strings floats so Python can process them, including decimals.
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

# Calculate the answer
p1 = x1+x2
p1 = p1/2
p2 = y1+y2
p2 = p2/2

# Display the answer to the user
print(f"Your answer is: ({p1},{p2})")