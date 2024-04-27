#creating a function to define the main part of the file using the keyword "main"
def main():
    age = input("What's your age? ")
main()
#create functions using the key word def
#an important note is that you must call a function at the top lines of your code since the python interpreter reads lines from top to bottom
#add the parameter to//"Who do you want to say hello to?"// add the to in the print statement so the function says hello to that variable in name
#you can set the parameter to to have a default value of "world" in the same line you're defining a function// just in case the user doesnt add a name
def hello(to="world"):
    print("Hello,", to)
#call hello 
hello()
name = input("What's your name? ")
#call the function and give it the user's input variable as an argument
#scope refers to variables only existing in the context in which you define them
#return is a key word used to literally return a value to you as the programmer
hello(name)