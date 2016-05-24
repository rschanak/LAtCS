"""Task 8: Replace {1,2,3} and {2,3,4} from the previous comprehension with two disjoint three-element sets so that the value becomes
   a five element set."""

S = {x*y for x in {5,15,0} for y in {1,1.0/3.0,3}}#SUCH A COOL ALGEBRA PROBLEM! Hint: Set it up like (x+y+z)(a+b+c)
print(S)