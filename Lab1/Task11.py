"""Task 11: Write a double list comprehension over the lists ['A','B','C'] and [1,2,3] whose list is the value 
of all possible two-element lists [letter,number]."""
print([[x,y] for x in ['A', 'B', 'C'] for y in [1,2,3]])