#create functions using the key word def
#add the parameter to//"Who do you want to say hello to?"// add the to in the print statement so the function says hello to that variable in name
def hello(to):
    print("Hello,", to)
name = input("What's your name? ")
#call the function and give it the user's input variable as an argument
hello(name)