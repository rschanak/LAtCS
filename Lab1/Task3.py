"""Task 3: Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3."""

a = ((673 + 909) % 3 == 0)
print(a)
#Everything below the above print statement is optional and only used to convey "proof."
print('The remainder is ' + str(673 + 909 % 3))#Shows that the remainder is in fact not 0.
print(type(a))#Shows that the statment 'a' is a Boolean statement.
