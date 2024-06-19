'''16. Make a program for a paint store. The program should ask for the size in square meters of the area to be painted. 
Consider that the paint coverage is 1 liter for every 3 square meters and that the paint is sold in 18-liter cans, which cost R$80.00. 
Inform the user of the quantities of paint cans to be purchased and the total price.'''

print("# Program to calculate how many liters of paint you need to paint a wall! #\n")

meters = float(input("Enter how many square meters of wall you want to paint: "))

liters = meters / 3

cans = (liters // 18) + 1

value = cans * 80

print("\nYou need {} cans to paint {} meters, paying a total of: {} reais.".format(cans, meters, value))