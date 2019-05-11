# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  Terminal Input
#
# PURPOSE:  This program will take values passed in via terminal command-line arguments.
# RUNTIME:  Python 2+

"""
IMPORTANT NOTE:  To run this program, the command-line needs to have arguments.  The typical command is:

python3 04_input_terminal.py John Smith
"""


import sys                              # used for command line processing

# get command-line arguments
first_name = sys.argv[1]
last_name = sys.argv[2]

# Say hello to this person
print("Hello, " + first_name + " " + last_name )