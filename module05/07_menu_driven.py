# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 June 14
# COURSE:   IT-140
# PROGRAM:  07 - Menu-driven program
#
# PURPOSE:  This is a menu-driven program that makes a function call
#           for each selection the user makes.
#
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Constant values for membership rate.  
# NOTE:  Constant values should be "read only", but that is not the case in Python.  To avoid this,
# do not change the value
ADULT_CHOICE = 1
CHILD_CHOICE = 2
SENIOR_CHOICE = 3
QUIT_CHOICE = 4

# Constants for membership rates
# NOTE:  Constant values should be "read only", but that is not the case in Python.  To avoid this,
# do not change the value
ADULT_CHOICE = 1
ADULT_RATE = 40.0
CHILD_RATE = 20.0
SENIOR_RATE = 30.0

# Define functions.  
# NOTE:  Function needs to be defined before it's called.
def show_menu():
    """ Displays them menu.
    """
    print("\n\t\tHealth Club Membershhip Menu\n")
    print("1.  Standard Adult Membership")
    print("2.  Child Membership")
    print("3.  Senior Citizens Membership")
    print("4.  Quit the program\n")
    print("Enter your choice:  ", end="")

def show_fees(member_rate, months):
    """ The member_rate paraemter holdss the monthly membership rate and
        the months parameter holds the number of months.  The function
        displays the total charges.
    """
    total_charge = float(member_rate) * int(months)
    print("The total charges are $" + "{:12.2f}".format(total_charge))

# Initialize menu choice
menu_choice = 0

# Setup a "do-while" loop.  Since Python doesn't support posttest loops,
# the menu_choice should be set to a value that is not 4 to force the
# while loop to run at least once, thus satisfying the design of a posttest
# loop.
while ( menu_choice != QUIT_CHOICE ):
    show_menu()
    menu_choice = int(input())

    # Validate menu choice
    while ((menu_choice < ADULT_CHOICE) or (menu_choice > QUIT_CHOICE)):
        menu_choice = int(input("Please enter a valid menu choice:  "))

    # Get membership term length if user has chosen a rate.
    if (menu_choice != QUIT_CHOICE):
        months = int(input("For how many months?  "))

        # Determine fees based on menu choice
        if menu_choice == ADULT_CHOICE:
            show_fees(ADULT_RATE, months)
        elif menu_choice == CHILD_CHOICE:
            show_fees(CHILD_RATE, months)
        elif menu_choice == SENIOR_CHOICE:
            show_fees(SENIOR_RATE, months)
        