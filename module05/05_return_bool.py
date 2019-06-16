
# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  03 - Arguments Example (Does not return value)
#
# PURPOSE:  This program will show a function that returns a boolean value.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Define function.  NOTE:  Function needs to be defined before it's called.
def isEven(number):
    """  This function will determine if a number is even or odd.

    Arguments:
        number -> value to be considered

    Returns:
        True -> Number is even
        False -> Numbe is odd
    """
    # Initialize status variable to empty (NULL) value
    status = None

    # Determine if number is even or odd
    if (number % 2 == 0):
        status = True
    else:
        status = False

    # return value of status
    return status

# Print program title
print("-----------------------------------------------------")
print("IS IT EVEN?")
print("-----------------------------------------------------")

# Have user enter a number to evaluate.
print("Enter an integer and I will tell you ")
val = int(input("if it is even or odd:  "))

# Determine if the number is even or odd by calling the isEven function.
if (isEven(val)):
    print(str(val) + " is even.")
else:
    print(str(val) + " is odd.")


