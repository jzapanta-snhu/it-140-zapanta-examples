# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  04 - 2-D Lists
#
# PURPOSE:  This program will demonstrate the use of a two-dimensional list
# RUNTIME:  Python 3+
#
# CREDITS:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ


# Initialize the list
table = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]   
]

# Output "table" to screen
print('The contents of "table" are:')
# For each row in the table list
for row in table:
    # For each column in the row list
    for col in row:
        # The code below basically sets up "cells" to allow for proper printing.
        # The goal is to print the column values next to each other until the row
        # is done processing.
        print('{:10}'.format(col), sep="", end="")
    # Print blank line to move the next row
    print()