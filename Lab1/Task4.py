"""Task 4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it to check your prediction."""

x = -9
y = 1/2 #0 due to integer division. 
y1 = 2**(y+1/2)#y(1/2) will print 0. 1/2 + 1/2 with integer division is 0! y(1/2) would print 2 if you used float division. 
y2 = 2**(y-1/2)#y(1/2) will also print 0, but even if you used float division it would print 0. 
if x + 10 < 10:#'1' is < 10, so it will print y1 which is 1. 
    y1 = str(y1)#Reassigning variable here.
    print('Using integer division: '+ y1)
else:
    y2 = str(y2)
    print('Using integer division: '+ y2)

#Following code is optional but added to illustrate point:
z = 1.0/2.0
y3 = 2**(z+(1.0/2.0))#Should read 2.
y4 = 2**(z-(1.0/2.0))#Should still read 1.
if x + 10 < 10:
    y3 = str(y3)
    print('Using float division: ' + y3)
else:#Not a needed line, as we know that y4 and y2 will never be used, none the less: adding it.
    y4 = str(y4)
    print('Using float division: ' + y4)