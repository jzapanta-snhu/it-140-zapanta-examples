# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 19
# COURSE:   IT-140
# PROGRAM:  05 - Pattern OUTPUT
#
# PURPOSE:  This program will print a pattern using nested for loops
#
# RUNTIME:  Python 3+

def main():
    """ Main function.
    """

    print ("05 - Pattern Output\n\n")

    for i in range(10):
        for j in range(10):
            print("*", sep="", end="")
        print()

# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()