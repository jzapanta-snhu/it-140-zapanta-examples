# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  Terminal Input
#
# PURPOSE:  This program will take values passed in via the keyboard.
# RUNTIME:  Python 2+
#
# Ask user to first and last name
first_name = input("Enter first name:  ")
last_name = input("Enter last name:  ")

# Ask user for favorite number.  Convert
favorite_number  = int(input("Enter your favorite number:  "))

# Say hello to this person and display their favorite number
print("\n\nHello, " + first_name + " " + last_name )
print ("Your favorite number is " + str(favorite_number))
print ("Your favorite number squred is " + str(favorite_number * favorite_number)) 