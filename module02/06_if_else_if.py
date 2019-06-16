# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     15 May 2009
# COURSE:   IT-140
# PROGRAM:  Numeric Test Scores
#
# PURPOSE:  Using if...elif, this program determines a letter grade based on a numeric value.
# RUNTIME:  Python 2+
#
# CREDIT:  Gaddis, T. (2012). Starting Out with C++: From Control Structures Through Objects. Pearson Addison-Wesley. Retrieved from https://books.google.com/books?id=Xbt0uQAACAAJ

# Define grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Display heading
print("NUMERIC TEST SCORES")

# Get the numeric test score
testScore = int(input("Enter your numeric test score and I will\ntell you the letter grade you entered"))

# Is the score greater than or equal to 90?
if (testScore >= A_SCORE):
    print("Your grade is A.")
# Is the score greater than or equal to 80?
elif (testScore >= B_SCORE):
    print("Your grade is B.")
# Is the score greater than or equal to 70?
elif (testScore >= C_SCORE):
    print("Your grade is C.")
# Is the score greater than or equal to 60?   
elif (testScore >= D_SCORE):
    print("Your grade is D.")
# You're probably not having a good grade date
elif (testScore >= 0):
    print("Your grade is F.")
# Is the score less than 0?
else:
    print("Invalid test score.")


