"""Task 5: Write a comprehension over {1,2,3,4,5} whose value is the set consisting of the square of the first five positive integers.
   Task 6: Write a comprehension over {0,1,2,3,4} whose value is the set consisting of the first five powers of two, starting at 0."""

S1 = {1,2,3,4,5}
S2 = {0,1,2,3,4}

print({x**2 for x in S1})
print({2**x for x in S2})
