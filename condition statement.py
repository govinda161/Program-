# Assignment Statement
number = 20
# Conditional Statement
if number >= 10:
    print("The number is greater than .\n")
else:
    print("The number is less than.\n")

    
# Taking input from the user
number = int(input("Enter a number: "))
# Using a ternary operator to check if the number is even or odd
if number % 2 == 0:
    print('Even','\n')
else:
        print("Odd",'\n')

        
# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Swapping the numbers
num1, num2 = num2, num1
# Display the swapped values
print('After swapping:','\n','First number:', num1,'\n','Second number:',num2,'\n')


# Conversion factor from kilometers to miles
conversion_factor = 0.621371
# Taking input from the user
kilometers = float(input("Enter distance in kilometers: "))
# Converting kilometers to miles
miles = kilometers * conversion_factor
# Display the result
print(kilometers ,'kilometers is equal to miles ',miles)


#amount
P = 200
# Rate of interest per year
R = 5
# Time period in years
T = 5
# Calculating Simple Interest
SI = (P * R * T) / 100
# Display the result
print(f"The Simple Interest on Rs. {P} for {T} years at {R}% per year is Rs. {SI}.\n")


# Demonstrating 'break' and 'continue' in a for loop
print("Demonstrating 'break' statement:")
for i in range(0, 8):
    if i == 5:
       break
    print(i)

    
print("\nDemonstrating 'continue' statement:")
for i in range(1, 8):
    if i == 5:       
       continue
    print(i)


