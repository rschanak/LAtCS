"""Task 2: Use Python to find the remainder of 2304811 divided by 47 without using the modulo operator %."""

a = 2304811
b = 47

#Use floor division to calculate what isn't the remainder.

floor_division = a // b
floor_multiplication = floor_division * 47 

remainder = a - floor_multiplication

print(remainder)