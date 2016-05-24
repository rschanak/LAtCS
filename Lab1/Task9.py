"""Task 9: Assume that S and T are assigned sets. Without the intersection operator &, write
   comprehension over S whose value is the intersection of S and T. Use S = {1,2,3,4} and T = {3,4,5,6}"""

S = {1,2,3,4}
T = {3,4,5,6}
print({x for x in S for y in T if x == y})