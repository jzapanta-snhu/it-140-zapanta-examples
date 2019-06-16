# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 19
# COURSE:   IT-140
# PROGRAM:  05 - Pattern OUTPUT
#
# PURPOSE:  This program will demonstrate an infinite loop
#
# RUNTIME:  Python 2+
#
# CREDITS:  Downey, A. B. (2012). Think Python. O’Reilly Media. Retrieved from https://books.google.com/books?id=10KYwCZxSdEC

print ("06 - Infinite Loop\n\n")
dummy = input("To end the program, hit CTRL + Break.  Press <ENTER> key to start the infinite loop.")

# Line 16 is bad...Very bad... :-(
while (True):
    print("Lather.")
    print("Rinse.")
    print("Repeat...")