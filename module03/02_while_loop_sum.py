# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 19
# COURSE:   IT-140
# PROGRAM:  02 - Summation Problem Using a WHILE Loop
#
# PURPOSE:  This program will calculate the summation of of a number from 1 to n,
#           where "n" is the values that has been entered.
#
# RUNTIME:  Python 2+

def main():
    """ Main function.
    """

    # Display header
    print ("02 - Summation Problem Using a WHILE Loop")

    # Display directions
    print("You will enter a number.  The program will calculate the sum from 1 to the number you enter.")

    # Get input value from keyboard.
    # PRECONDITION:  We will assume the user will enter a positive number, but this
    # should be addressed in code...Perhaps in the next example... :-)

    number = int(input("Enter a whole number greater than 0:  "))
    
    # Setup accumulator variable that will hold the sum
    sum = 0
    while (number > 0):
        sum = sum + number              # Update sum with the value of sum plus the current value of number
        number = number - 1             # Decrement value of number by 1

    # Display results
    print( "Sum:  ", sum)



# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()