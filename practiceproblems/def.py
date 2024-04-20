#create functions using the key word def
#add the parameter to//"Who do you want to say hello to?"// add the to in the print statement so the function says hello to that variable in name
#you can set the parameter to to have a default value of "world" in the same line you're defining a function// just in case the user doesnt add a name
def hello(to="world"):
    print("Hello,", to)
#call hello 
hello()
name = input("What's your name? ")
#call the function and give it the user's input variable as an argument
hello(name)