# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     15 May 2009
# COURSE:   IT-140
# PROGRAM:  Loan Qualification
#
# PURPOSE:  This program will demonstrate nested if statements
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

def main():
    """ Main function 
    """

    # Display program heading
    print("LOAN QUALIFICATION PROGRAM")
    print()                             # Just another way to add an extra line break
    print ("Please answer the following questions")
    print ("with either Y for Yes or N for No.")

    # Get responses to loan qualification questions
    employed = input("Are you employed? ")
    recent_grad = input("Have you graduated from college in the past two years? ")

    # Are you employed?
    if (employed == 'Y'):
        # If employed, are you a recent college graduate?
        if (recent_grad == 'Y'):
            print("You qualify for the special interest rate.")
        else:
            print("You must have graduated from college in the past two\nyears to qualify.\n")
    else:
        print ("You must be employed to qualify.")
   

# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()