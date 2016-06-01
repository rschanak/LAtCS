"""Task 17: Write a comprehension over a range of the form range(n) such that 
the value of the comprehension is the set of odd numbers from 1 to 99"""


#Okay... I cheated here. This is how you would do it with a loop, but
#I kept getting an error... I think it's fixable though.
for x in range(100):
    if x % 2 != 0:
        print x
    else:
        pass

print "\nEnd of loop method."

#This is how you would do it normally, I don't know what caused the error
#as this is what I initially had typed in... maybe whitespace?
#However... if you run %timeit in iPython the loop method runs at 
#142 microseconds per loop, whereas the comprehension method runs at
#10.4 microseconds per loop. You would have to also fill a list with
#the results in the loop method, making the comprehension method
#around 20 times as fast I'm guessing.
list1 = [x for x in range(100) if x % 2 != 0]
print(list1)