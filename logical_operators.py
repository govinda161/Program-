# and Operator
'''The and operator returns True if both operands are true.'''
a = 10
b = 20

if a > 5 and b > 15:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")


# or Operator
'''The or operator returns True if at least one of the operands is true.'''
a = 10
b = 5

if a > 15 or b < 10:
    print("At least one condition is true.")
else:
    print("Both conditions are false.")


# not Operator
'''The not operator reverses the boolean value of the operand.'''
a = False

if not a:
    print("a is False.")
else:
    print("a is True.")


# Combined Example
# Input value
a = 10
b = 5
c = 15

if (a > b and b < c) or (a < 5 and not c == 15):
    print("Complex condition is true.")
else:
    print("Complex condition is false.")
