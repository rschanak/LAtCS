"""Task 4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it to check your prediction."""

x = -9
y = 1/2 #0 due to integer division. 
y1 = 2**(y+1/2)#y(1/2) will print 0. 1/2 + 1/2 with integer division is 0! y(1/2) would print 2 if you used float division. 
y2 = 2**(y-1/2)#y(1/2) will also print 0, but even if you used float division it would print 0. 
if x + 10 < 10:#'1' is < 10, so it will print y1 which is 1. 
    print(y1)
else:
    print(y2)