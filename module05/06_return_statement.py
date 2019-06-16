# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  06 - Arguments Example (Does not return value)
#
# PURPOSE:  This program demonstrates the use of the "return" statement to return (pun somewhat intended)
#           control to the statement that called the function in the event the function needs to end
#           (typically prematurely).
#
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Define function.  NOTE:  Function needs to be defined before it's called.
def divide(arg1, arg2):
    """ Definition of function divide
    Uses two parameters: arg1 and arg2.  The function divides arg1
    by arg2 and shows the result.  If arg2 is zero, however, the
    function returns without completing the calcuation.
    """
    if (float(arg2) == 0.00):
        print("Sorry, I cannot divide by zero.")
        return
    else:
        print ("The quotient is", (arg1 / arg2 ))

# Provide instructions to user.
print("Enter two numbers and I will divide the first")
print("number by the second number.\n")

# Get numbers to calculate
num1 = float(input("First number:  "))
num2 = float(input("Second number:  "))

# Call "divide" function.
divide(num1, num2)