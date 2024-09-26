# Example of using break
''' The break statement is used to exit the loop prematurely when a certain condition is met. '''
for num in range(1, 11):
    if num == 6:
        print("Breaking the loop at 6.\n")
        break
    print(num)


# Example of using continue
''' The continue statement skips the current iteration and moves to the next iteration of the loop. '''
for num in range(1, 11):
    if num % 2 == 0:
        print(f"Skipping even number: {num}")
        continue
    print(num)


# Example using both break and continue
for num in range(1, 11):
    if num == 3:
        print("Skipping number 3.")
        continue  # Skip this iteration
    if num == 8:
        print("Breaking the loop at 8.")
        break  # Exit the loop
    print(num)
