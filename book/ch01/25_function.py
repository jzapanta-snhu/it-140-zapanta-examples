# NAME: 	Javier Zapanta (j.zapanta@snhu.edu)
# DATE:		09 May 2019
# COURSE: 	IT-140
# PROGRAM: 	Chapter 1 - Function Example
# PURPOSE:  	This program will demonstrate how a custom-made function works.
# RUNTIME:	Python 3+

def applyDiscount(price, discountRate):
	""" Function will calculate discounted price 
	
		This functiosn will take the price and discount rate as a decimal and calculate the new price.
		
		Parameters:
		price (float):  Price of item.
		discountRate (float):  Discount rate a decimal (rate / 100).
		
		Returns:
		float:  Calculated price with discount in effect.
	"""

	# calculate sale price and return result to original function call (Line 33)
	return price - (price * discountRate)

# initialize salePrice and discount
salePrice = 29.99						# price
discount = 0.10							# percentage as decimal

print ("SALE PRICE CALCULATION\n")
# Use of sep="" gets rid of the default separator when using a comma in a print statement to
# combine an output stirng.
print ("Price: $", salePrice, sep="")
print ("DiscountRate:  ", (discount * 100), "%", sep="")
print ("Discounted price:  $", applyDiscount(salePrice, discount), sep="")
