# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  02 - My First Return Function
#
# PURPOSE:  This program will print a string returned from a function.
# RUNTIME:  Python 2+

# Define function.  NOTE:  Function needs to be defined before it's called.
def my_first_return_function():
    """ This function will build a string and have its value returned.
    """
    # Build string.
    string = "Hello World!\n"
    string += "That's all folks"
    # Return value of string.
    return string

# Store value returned from my_first_return_function()
message = my_first_return_function()

print (message)

print ("-----------------------")

# Just print the value returned from my_first_return_function()
print (my_first_return_function())