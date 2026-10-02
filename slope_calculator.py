# Slope Calculator
# Written by Sean-e on Wednesday, September 30th, 2026
# Last updated on Friday, October 2nd, 2026

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

# Display the answer to the user
ys = y2-y1
xs = x2-x1
print("Your answer is:")
print(ys)
print("-----")
print(xs)
print(f"Your divided answer is: {ys/xs}")