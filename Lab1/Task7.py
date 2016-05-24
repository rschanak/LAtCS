"""Task 7: The value of the comprehension: {x*y for x in {1,2,3} for y in {2,3,4}} is a seven-element set. 
   Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set."""

S1 = {x*y for x in {1,3,5} for y in {7,11,13}}
print(S1)