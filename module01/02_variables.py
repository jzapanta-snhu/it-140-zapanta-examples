# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  Variables
#
# PURPOSE:  This program will the use of simple variables.
# RUNTIME:  Python 2+
#
# CREDIT:  McGrath, M. (2003). C++ Programming in Easy Steps. Dreamtech Press. Retrieved from https://books.google.com/books?id=m8Ubu-eSqyIC

num = 100
string1 = 'Z'
string2 = "Another string"
string3 = '''Another "stirng"'''
pi = 3.14159
boolean_flag = True

# Format using a dot opeator function call to "format" and using alias for position ({first})
print ("num:\t {first}".format(first=num))

# print by appending string
print ("string1:\t" + string1)

# pring by appending with comma
print ("string2:\t", string2)

# Format using a dot opeator function call to "format"
print ("string1:\t {}".format(string3))

# Print by appending string and converting floating-point number to string.
# When outputing a concatenated string, a number must be converted to a string.
print ("pi:\t" + str(pi))

# Output result of boolean variable as numeric (%d) value
print ("boolean_flag:\t%d" % boolean_flag)

# Output result of boolean variable as string (%s) value
print ("boolean_flag:\t%s" % boolean_flag)