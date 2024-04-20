#a float is an integer with a decimal more properly referred to as a floating point value

#they are "real numbers"

#use the float function instead of the int function to specify the variable's data type

a = float(input("What is a? "))

b = float(input("What is b? "))

print(a + b)

#use the round function to round the inputs to the nearest integer// the actual python docs for this function is round(number[, ndigits]) round --> number argument --> optional specification in brackets

a = float(input("What is a? "))

b = float(input("What is b? "))

c = round(a + b)

print(f"{c:,}")