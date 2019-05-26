# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  01 - FOR Loop Examples
#
# PURPOSE:  This program will take values passed in via terminal command-line arguments.
# RUNTIME:  Python 2+

def main():
    """ Main function.
    This function will demonstrate hte for loop outputting the value of the counter variable.
    """

    # Display header
    print ("01 - FOR Loop Examples")


    # Print heading for first example
    print("\n\n*************************************************************************************************")
    print("Example #1:  Range with start, stop and step.")
    print("*************************************************************************************************")

    # Setup range (start, stop, step)
    #
    # start_of_range - the starting index of the range
    # end_of_range - the ending index of the range (stop - step is the actual end.  So if stop = 4 and step is 1, then 3 is the real stop value)
    # step_value - the increment between values in a range
    #
    start_of_range = 1
    end_of_range = 4
    step_value = 1


    for i in range(start_of_range, end_of_range, step_value):
        print("---------------------------------------------------------------------------------------------")
        print("We have started a new iteration of the loop and we're going to print out the new value of i.")
        print(i)
        print("We're not going to increment the range by", step_value)
        print("---------------------------------------------------------------------------------------------")

    # Print heading for first example
    print("\n\n*************************************************************************************************")
    print("Example #2:  RanAnother range with start, stop and step.")
    print("*************************************************************************************************")

    # Setup range (start, stop, step)
    #
    # start_of_range - the starting index of the range
    # end_of_range - the ending index of the range (stop - step is the actual end.  So if stop = 0 and step is -1, then 1 is the real stop value)
    # step_value - the increment between values in a range
    #
    
    start_of_range = 4
    end_of_range = 0
    step_value = -1

    for i in range(start_of_range, end_of_range, step_value):
        print("---------------------------------------------------------------------------------------------")
        print("We have started a new iteration of the loop and we're going to print out the new value of i.")
        print(i)
        print("We're not going to increment the range by", step_value)
        print("---------------------------------------------------------------------------------------------")

    # Print heading for second example
    print("\n\n*************************************************************************************************")
    print("Example #3:  Range with stop value.")
    print("*************************************************************************************************")

    # Another range example.  This start value is defaulted to 0.  The step value is defaulted to 1.

    range_size = 4

    for j in range(range_size):
        print("---------------------------------------------------------------------------------------------")
        print("We have started a new iteration of the loop and we're going to print out the new value of i.")
        print(j)
        print("By default the step by value will increment by 1")
        print("---------------------------------------------------------------------------------------------")



# See https://runestone.academy/runestone/static/thinkcspy/Functions/mainfunction.html
#
# call main function if this is the main file
if __name__ == "__main__":
    # Go to Line 28 when "main" is called
    main()