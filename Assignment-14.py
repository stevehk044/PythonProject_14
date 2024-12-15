def power(base, exponent):
    return base ** exponent

# Prompt the user to enter the base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
result = power(base, exponent)

# Display the result
print(f"{base} raised to the power of {exponent} is {result}")
