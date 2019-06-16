# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 19
# COURSE:   IT-140
# PROGRAM:  04 - Sentinel Value
#
# PURPOSE:  This program will calculate the summation of of a number from 1 to n,
#           where "n" is the values that has been entered.
#
# RUNTIME:  Python 3+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

game = 1                            # Game counter
points = 0                          # To hold number of points
total = 0                           # Accumulator that will hold total points.

# Print Heading
print("04 - Sentinel Value\n")

print ("Enter the number of points your team has earned")
print ("so far in the season, then enter -1 when finished.\n")
points = int(input("Enter the points for game " + str(game) + ":  "))

while (points != -1):
    total = total + points
    game = game + 1
    points = int(input("Enter the points for game " + str(game) + ":  "))

print("\nThe total points are " + str(total))

