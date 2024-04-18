name = input("What is your name?")

#strip is a string method used to remove white space

name = name.strip()

#most basic variable and function program by asking the user for their name

#input only takes strings

#when you insert multiple arguments to print, it will automatically add a space

print("hello, ", end="" )

print(name)

#the print function can take any number of objects using the * syntax

#by default, the print function ends with \n

#print(*objects, sep=' ', end='\n', file=None, flush=False)

#backslashes inside inner double quotes help the computer realize that those quotes dont finish a line referred to as "escaping"


print("hello, \"friend\"")

#format string

print(f"hello, {name}")