"""Task 16: Find an example of a list L such that len(L) and len(list(set(L))) are different."""

L = [1,1,2,3]#in general, L = [n(1), n(2), n(3), ..., n(n-1), n(n), n(n)]

print L
print len(L)
print len(list(set(L)))