x = int(input("What's x? "))

y = int(input("What's y? "))
#think about adding boolean or true or false values to these using this if statement
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
#add the keyword elif that creates a loop
#else is a "Catch all" for the final possibility
#if x > y:
    #print("x is greater than y")
#if x < y:
    #print("x is less than y")
#if x == y:
    #print("x is equal to y")
#adding the or
#if x < y or x > y:
    #print("x is not equal to y")
#else:
    #print("x is equal to y")
#the best way to program this 
#!= stands for "does not equal"; the exclamation point changes the assignment operator
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")