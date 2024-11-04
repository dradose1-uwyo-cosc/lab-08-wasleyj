# Wesley Jones
# UWYO COSC 1010
# 11/04/24
# Lab 8
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_num(input_string):
    try:
        output=int(input_string)
    except:
        try:
            output=float(input_string)
        except:
            print("this is not a valid interger or float.")
    return(output)    

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m,b,lx,ux):
    """y=mx+b lx=lower x ux=upper x"""
    y=[]
    try:
        int(lx)
        int(ux)
    except:
        print("you can only input integers for upper and lower bounds")
    else:
        for x in range(int(lx),int(ux)+1):
            y.append(int(m)*x+int(b))
        return(y)

#print(slope_intercept(5,10,0,10))
while True:
    a=0
    b=0
    lb=0
    ub=0
    print("enter q to quit at any time")
    a=input("please insert a number for m (the slope):\n")
    if a=="q":
        break
    else:
        b=input("please insert a number for b (the intercept):\n")
        if b=="q":
            break
        else:
            lb=input("please insert a integer number for lx (the lower bound):\n")
            if lb=="q":
                break
            else:
                ub=input("please insert a integer number for ux (the upper bound bound):\n")
                if ub=="q":
                    break
                else:
                    print(slope_intercept(a,b,lb,ub))


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
print("We are now going to slove the quadratic formula!\n(enter q to quit at any time)\n")

def sqrt(s):
    if s < 0:
        return("null")
    w=s**0.5
    return(w)

def quad_form(a,b,c):
    try:
        int(a) and int(b) and int(b)
    except:
        print("You did not enter numbers!")
    else:
        if (int(b)**2)-4*int(a)*int(c) < 0:
            print("*" * 75)
            print("You cant take the square root of a negative!")
            print("*" * 75)
        x1=(-int(b)+sqrt((int(b)**2)-4*int(a)*int(c)))/2*int(a)
        x2=(-int(b)-sqrt((int(b)**2)-4*int(a)*int(c)))/2*int(a)
        return(x1,x2)
    
while True:
    "enter q to quit this function"
    a=input("insert a number to assign to the variable a:\n")
    if a=="q":
        break
    b=input("insert a number to assign to the variable b:\n")
    if b=="q":
        break
    c=input("insert a number to assign to the variable c:\n")
    if c=="q":
        break
    print(f"Your Answers are:\n{quad_form(a,b,c)}")