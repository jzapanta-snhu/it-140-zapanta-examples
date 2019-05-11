# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  Terminal Input
#
# PURPOSE:  This program will demonstrate a function that returns a value.
# RUNTIME:  Python 2+
#
# CREDIT:   Gaddis, T. (2010). Starting Out with C++: From Control Structures through Objects, Brief Version Custom Edition for NHTI - Concord’s Community College (Custom 7th). Boston, MA: Pearson Education, Inc.

def sum(num1, num2):
    """ Function calculates the sum of two numbers
    
        The function will accept two numbers as arguments
        and return the sum of the two values.

        Arguments:
        num1 (int):  First number
        num2 (int):  Second number

        Returns:
        int:  Calculated sum.
    """

    # calculate result as part of return statement
    return num1 + num2

# initialize values
value1 = 20
value2 = 40

# Call the sum function, passing the contents of
# value1 and value2 as arguments.  Assign the return
# value to the total variable
total = sum(value1, value2)

# Display the sum of the values
print("Thum sum of " + str(value1) + " and " + str(value2) + " is " + str(total))