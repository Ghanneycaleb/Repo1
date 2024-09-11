#Variables: act as stores of values


# Prompt the user for input and store the value in variable 'a'
a = input("a: ")

# Prompt the user for input and store the value in variable 'b'
b = input("b: ")

# Store the value of 'a' in a temporary variable 'c' to perform the swap
c = a

# Assign the value of 'b' to 'a', effectively swapping
a = b

# Assign the value stored in 'c' (original 'a') to 'b', completing the swap
b = c

# Print the new value of 'a'
print("a= " + a)

# Print the new value of 'b'
print("b= " + b)
