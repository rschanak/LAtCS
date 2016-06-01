"""Task 12: Suppose LofL has been assigned a list whose elements are themselves a list of numbers.
Write an expression that evaluates to the sum of all numbers in all the lists. The expression has the form:
sum([sum(...)]) and includes on comprehension."""

LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]

sum1 = sum([sum(LofL[i]) for i in range(len(LofL))])

print sum1