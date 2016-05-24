"""Task 7: The value of the comprehension: {x*y for x in {1,2,3} for y in {2,3,4}} is a seven-element set. 
   Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set."""



#Sets in Python, just like in Mathematics, contain unique elements. For example: 
a = {1,1,1,2,3}
print(a)
#Will only print {1,2,3} because those are the only unique elements. 
b = {x*y for x in {1,2,3} for y in {2,3,4}}#Is a seven element set because 2*3 and 3*2 are not unique (6 and 6).

S1 = {x*y for x in {1,3,5} for y in {7,11,13}}#The product of two primes are unique as they are the only factors made up of that number.
print(S1)