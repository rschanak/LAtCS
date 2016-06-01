"""Task 19: Starting from the lists [10, 25, 40] and [1, 15, 20], write a 
   comprehension whose value is the three-element list in which the first 
   element is the sum of 10 and 1, the second is the sum of 15 and 25
   and the third is the sum of 40 and 20. Use zip but not list."""


a = [10, 25, 40]
b = [1, 15, 20]



sums = [x + y for (x,y) in zip(a,b)]
print(sums)