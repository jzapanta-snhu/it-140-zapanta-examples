# NAME:     Javier E. Zapanta (j.zapanta@snhu.edu)
# DATE:     2019 May 10
# COURSE:   IT-140
# PROGRAM:  02 - Lists & Loops
#
# PURPOSE:  This program will initialize a list and print results using a loop.
# RUNTIME:  Python 2+

# Initialize a dictionary
my_dictionary = {
        'id': '47988'
    ,   'lastname': 'Picard'
    ,   'firstname': 'Jean-Luc'
    ,   'major_code': 'BUSI'
    ,   'major_text': 'Business'
}

# Print the dictionary
print(my_dictionary)
print()                                  # insert blank line


# Change the major
my_dictionary['major_code'] = 'PHIL'
my_dictionary['major_text'] = 'Philosophy'

# print the dictionary
print(my_dictionary)
print()                                  # insert blank line

# Let's print the ID number only
print(my_dictionary['id'])
print()                                  # insert blank line


# Let's print each key individually
for key in my_dictionary:
    print (key)

# Let's print each value individually using the value variable and key
# NOTE:  We must set key first, even though it's not being used.
for key, value in my_dictionary.items():
    # Print the value
    print (value)
    # Print the value using the key
    print (my_dictionary[key])

print() 

# Let's print the key and value
for key, value in my_dictionary.items():
    # Print the key and value
    print(key + ":  " + value)