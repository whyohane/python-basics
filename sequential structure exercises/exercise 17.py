'''17. Make a Program for a paint store. The program should ask for the size in square meters of the area to be painted. 
Consider that the paint coverage is 1 liter for every 6 square meters and that the paint is sold in 18-liter cans, which cost R$80.00 or in 3.6-liter gallons,
which cost R$25.00 .
Inform the user of the quantities of paint to be purchased and the respective prices in 3 situations:
1- buy only 18 liter cans;
2- buy only 3.6 liter gallons;
3- mix cans and gallons, so that paint waste is less. Add 10% slack and always round the values ​​up, that is, consider full cans.'''

meters = float(input("Enter how many square meters of wall you want to paint: "))

liters = meters / 6

# First case: Apenas latas de 18 litros.
bigCans = (liters // 18) + 1

totalValue = bigCans * 80

print("You can buy {} large cans to paint {} meters, paying a total of: {} reais. \n".format(bigCans, meters, totalValue))

# Segundo caso: Apenas latas de 3,6 litros.
smallCans = (liters // 3.6) + 1

totalValue = smallCans * 25

print("You can buy {} small cans to paint {} meters, paying a total of: {} reais. \n".format(smallCans, meters, totalValue))

# Terceiro caso: Misturar ambas as latas.
if liters < 18:
    smallCans = (liters// 3.6) + 1
    totalValue = smallCans * 25
    print ("You can buy just {} small cans, paying {} reais. \n".format(smallCans, totalValue))
else:
    bigCans = 0
    smallCans = 0

    while liters >= 18 :
        bigCans += 1
        liters = liters - 18
    
    while liters > 0 :
        smallCans += 1
        
        if liters < 3.6 :
            smallCans += 1
            liters = 0
        else :  
            liters = liters - 3.6

    totalValue = (bigCans * 80) + (smallCans * 25)
    print("You can buy {} large cans and {} small cans, paying a total of {} reais. \n".format(bigCans, smallCans, totalValue))