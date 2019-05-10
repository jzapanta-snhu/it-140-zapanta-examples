# NAME: 	Javier Zapanta (j.zapanta@snhu.edu)
# DATE:		09 May 2019
# COURSE: 	IT-140
# PROGRAM: 	Chapter 1 - Function Example
# PURPOSE:  This program will demonstrate how a custom-made function works.

def applyDiscount(price, discountRate):
	""" Function will calculate discounted price 
	
		This function will take the price and discount rate as a decimal and calculate the new price.
		
		Parameters:
		price (float):  Price of item.
		discountRate (float):  Discount rate a decimal (rate / 100).
	"""
	return price - (price * discountRate)

# setup sale Price and discount
salePrice = 29.99
discount = 0.10

print ("SALE PRICE CALCULATION\n")
print ("Price: $", salePrice)
print ("DiscountRate:  ", (discount * 100), "%")
print ("Discounted price:  $", applyDiscount(salePrice, discount))
