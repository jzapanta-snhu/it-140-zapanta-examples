# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  02 - Lists & Loops
#
# PURPOSE:  This program will initialize a list and print results using a loop.
# RUNTIME:  Python 2+

# Initialize a list
jerseyNumbers = [ 44, 8, 24, 32, 42, 33 ]

# EXAMPLE #1
#
# Print the list using a list item variable
# (This is the approach that you see in the text)
for jersey in jerseyNumbers:
    # Print jersey number
    print(jersey)

# Print blank line
print()

# EXAMPLE #2
#
# Print the list from the beginning of the list using subscripts
for i in range(len(jerseyNumbers)):
    # Print jersey number
    print(jerseyNumbers[i])

# Print blank line
print()

# EXAMPLE #3
#
# Print he list from the end of the list using subscripts
#
# Range arguments:
#   len(jerseyNumbers) - 1:  Starting index which is length of list -1, or 5
#   -1:  Stopping point.  It's negative 1 because we must include 0.
#   -1:  Step Value.  We have to decrement by 1
#
for j in range(len(jerseyNumbers) - 1, -1, -1):
    # Print jersey number
    print(jerseyNumbers[j])

# Print blank line
print()


# EXAMPLE #4
#
# Print list using a while loop from the beginning of the list
#
# Initialize size of list
size = len(jerseyNumbers)
# Initialize counter
counter = 0
while (counter < size):
    # Print jersey number
    print(jerseyNumbers[counter])
    # Increment counter
    counter = counter + 1

# Print blank line
print()

# Set counter value to size of jerseyNumbers - 1
counter = len(jerseyNumbers) - 1
while (counter >= 0):
    # Print jersey number
    print(jerseyNumbers[counter])
    # Decrement counter
    counter = counter - 1