#there are no decimal points in integers-- that is what the float data type is for

#python supports these symbols: + - * / %

#% sign is the modulas operator meaning that it gives the remainder of a division problem. For example, 5%2 is 1 since one is the remainder

#python supports an interactive mode that enables the programmer to write lines of code and immediately execute it

x = 1

y = 2

z = (x + y)

print(z)

#getting input from user gives you a string 

a = input("What is a? ")

b = input("What is b? ")

c = (a + b)

print(c)

#use int

a = input("What is a? ")

b = input("What is b? ")

c = int(a) + int(b)

print(c)

#nesting int and input functions 

a = int(input("What is a? "))

b = int(input("What is b? "))

print(a + b)