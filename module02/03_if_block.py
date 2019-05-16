# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 14
# COURSE:   IT-140
# PROGRAM:  High Score Error
#
# PURPOSE:  This program demonstrates the use of an if block with multiple statements.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

def main():
    """ Main function 
    """

    # Initialize high score
    HIGH_SCORE = 95

    # Display heading
    print("HIGH SCORE PROGRAM REVISITED\n")

    # Display instructions
    print("Enter 3 test scores and I will average them")

    # Get test scores.
    # NOTE: Using "input" function to get input from keyboard.
    # We will assume that data entered will be numerical test scores.
    score1 = float(input("Score 1:  "))
    score2 = float(input("Score 2:  "))
    score3 = float(input("Score 3:  "))

    # Calculate the average and display results
    average = (score1 + score2 + score3) / 3.0
    print ("Your average is " + str(average))

    # If the average is a high score, congratulate the user
    # Multiple statements that are part of the if block must be indented.
    if (average > HIGH_SCORE):
        print ("Congratulations!")
        print ("That's a high score.")
        print ("You deserve a pat on the back!")


# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()