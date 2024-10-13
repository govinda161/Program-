try:
    user_age = int(input("Enter your age: "))  # Convert input to an integer
    # Check if the user is eligible to vote
    if user_age>=18:
        print("You are eligible to vote.")  # Message for eligible voters
    else:
        print("You are not eligible to vote.")  # Message for non-eligible voters
except ValueError:
    print("Please enter a valid age.")  # Handle cases where input is not a valid integer
