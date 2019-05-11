# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  Main function.
#
# PURPOSE:  This program will demonstrate the use of a main function, along with a supporting function
# RUNTIME:  Python 2+
#
# CREDIT:   Gaddis, T. (2010). Starting Out with C++: From Control Structures through Objects, Brief Version Custom Edition for NHTI - Concord’s Community College (Custom 7th). Boston, MA: Pearson Education, Inc.

# Functions "first" and "second" have to be defined first so that they
# can be seen by the "main" function

def first():
    """  Definition of function first

        This function displays a message.
    """
    print ("I am now inside the function first.\n")

def second():
    """  Definition of function first

        This function displays a message.
    """
    print ("I am now inside the function first.\n")

def main():
    print ("I am starting in function main.")
    # call function first (Line 14)
    first()
    # call function second (Line 21)
    second()
    print("Back in function main again.")

# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()
