# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  01 - Hello World Function
#
# PURPOSE:  This program will print a string to the screen based on a function call.
# RUNTIME:  Python 2+

# Define function.  NOTE:  Function needs to be defined before it's called.
def my_first_function():
    """ This function will print a concatentated string message of:
    Hello World!
    That's all folks

    The function will not return a value.
    """
    string = "Hello World!\n"
    string += "That's all folks"
    print(string)

# call function
my_first_function()
