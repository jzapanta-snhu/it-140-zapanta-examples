# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 06
# COURSE:   IT-140
# PROGRAM:  Odd/Even
#
# PURPOSE:  This program will determine if an integer is odd or even.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ


# Display program heading
print("ODD OR EVEN")
print()                              # Just another way to add an extra line break
print ("Enter an integer and I will tel l you if it\nis odd or even.")
# We will assume that input will be an appropriate integer
number = int(input("Enter number:  "))

# determine if number is even using modulus division
if (number % 2 == 0):
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")