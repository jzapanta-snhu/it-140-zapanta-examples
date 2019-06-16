
# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  03 - Arguments Example (Does not return value)
#
# PURPOSE:  This program will accept two arguments to perform a math calculation.  The
#           result WILL be returned.
# RUNTIME:  Python 2+

# Define function.  NOTE:  Function needs to be defined before it's called.
def pow(x, y):
    """ This function will return the result of 'x' raised to the 'y' power.

    IMPORTANT NOTE:  This is a bad example because Python has a pow function
    and this is just a recreation of it.  The goal is to focus on the idea
    that we can accept values as arguments and use them to complete a
    given task
    """
    # Return result of 'x' to the 'y' power.
    return ( x ** y )

# Initialize variables
a = 2
b = 3

# Send a & b to pow, which will become x & y, respectively.
# The result will be returned from Line 21 and stored in results
# on Line 30.
result = pow(a, b)

# Print calculation result calculated from the function call on Line 30.
print (result)