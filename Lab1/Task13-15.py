"""Task 13: Suppose S is a set of integers, e.g. {-4,-2, 1,2,5,0}. Write a triple comprehension whose 
value is a list of all three-element tuples (i,j,k) such that i,j,k are elements of S whose sum is zero."""

S = {-4, -2, 1, 2, 5, 0}

sum_set = [(i,j,k) for i in S for j in S for k in S if i + j + k == 0]

print sum_set
#If you enter this into a shell without print or a variable
#this works fine. However, for some unknown reason to me, it won't work
#unless you have a print command *somewhere*. 

"""Task 14: Modify the comprehension in the previous task so that the resulting list does not include
(0,0,0) Hint: add a filter."""

print "\nEnd of first set of sums. \n"

sum_set2 = [(i,j,k) for i in S for j in S for k in S if i + j + k == 0 | i != 0 and j !=0 and k != 0]
print sum_set2

print "\nEnd of second set of sums. \n"

#Added the print "end of..." to not flood the terminal so much.

"""Task 15: Further modify the expression so that its value is not the list of all such tuples
but is the first such tuple."""


print("First Tuple " + str(sum_set2[0]))#This is a cheap fix that perhaps I'll remedy... some day...

