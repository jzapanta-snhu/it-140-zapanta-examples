# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     15 May 2009
# COURSE:   IT-140
# PROGRAM:  Loan Qualification
#
# PURPOSE:  This program demonstates the use of a menu.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Define membership rates
ADULT_RATE = 40.0
SENIOR_RATE = 30.0
CHILD_RATE = 20.0

# Define menu choices
ADULT_MENU_CHOICE = 1
CHILD_MENU_CHOICE = 2
SENIOR_MENU_CHOICE = 3
EXIT_PROGRAM_MENU_CHOICE = 4

# Display the menu
print ("\t\tHealth Club Membership Menu\n")
print("1.  Standard Adult Membership")
print("2.  Child Membership")
print("3.  Senior Citizen Membership")
print("4.  Quit the Program\n")
choice = int(input("Enter your choice:  "))

# Is this an adult membership?
if (choice == ADULT_MENU_CHOICE):
    months = int(input("For how many months?  "))
    charges = months * ADULT_RATE
    print("The total charges are $", charges, sep ="")
# Is this a child membership?
elif(choice == CHILD_MENU_CHOICE):
    months = int(input("For how many months?  "))
    charges = months * CHILD_RATE
    print("The total charges are $", charges, sep ="")
# Is this a senior citizen membership?       
elif(choice == SENIOR_MENU_CHOICE):
    months = int(input("For how many months?  "))
    charges = months * SENIOR_RATE
    print("The total charges are $", charges, sep ="")
# Do you want to quit the program?
elif(choice == EXIT_PROGRAM_MENU_CHOICE):
    print("End program...")
# Invalid data was entered
else:
    print("The valid choices are 1 through 4.  Run the")
    print("program again and select one of those")