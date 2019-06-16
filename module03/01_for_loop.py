# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  01 - FOR Loop Examples
#
# PURPOSE:  This program will take values passed in via terminal command-line arguments.
# RUNTIME:  Python 2+

# Display header
print ("01 - FOR Loop Examples")


# Print heading for first example
print("Example #1:  Range with start, stop and step.")

# Setup range (start, stop, step)
#
# start - the starting index of the range
# end - the ending index of the range (stop - step is the actual end.  So if stop = 4 and step is 1, then 3 is the real stop value)
# step - the increment between values in a range
#
for i in range(1, 4, 1):
    print(i)

# Print heading for first example
print("Example #2:  RanAnother range with start, stop and step.")

# Setup range (start, stop, step)
#
# start - the starting index of the range
# end - the ending index of the range (stop - step is the actual end.  So if stop = 0 and step is -1, then 1 is the real stop value)
# step - the increment between values in a range
#
for i in range(4, 0, -1):
    print(i)

# Print heading for second example
print("Example #3:  Range with stop value.")

# Another range example.  This start value is defaulted to 0.  The step value is defaulted to 1.
for j in range(4):
    print(j)
