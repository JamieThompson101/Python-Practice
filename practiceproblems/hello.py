name = input("What is your name?")

#strip is a string method used to remove white space

name = name.strip()

#.capitalize only capitalizes the first letter in the string

name = name.capitalize()

#.title is a method utilized to captilize user's input// a method is a function that is built into a data type

name = name.title()

name = name.strip().title()

#get the users input, capitalize everything, and strip away any white space

#you can string multiple methods together 

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

#best way to write this

name = input("What's your name? ").strip().title()

#and then print it to the terminal

print(f"hello, {name}")