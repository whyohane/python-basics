'''15. Create a program that asks how much you earn per hour and the number of hours worked in the month. Calculate and show your total salary for that month, knowing that 11% are deducted for Income Tax, 8% for INSS and 5% for the union, create a program that gives us:
gross salary.

1- how much you paid to INSS.
2- how much he paid to the union.
3- net salary.'''

print("# Program to calculate your salary and applied discounts! #\n")

earnHour = float(input("How much you earn per hour? "))
hour = float(input("How many hours you work per month? "))

grossSalary = earnHour * hour

discountINSS = (8/100 * grossSalary)

discountSind = (5/100 * grossSalary)

discountIR = (11/100 * grossSalary)

netSalary = grossSalary - discountINSS - discountIR - discountSind

print("\n30Your gross salary is: ", grossSalary)
print("You pay {} reais for INSS. \n".format(discountINSS))
print("You pay {} reais for IR. \n".format(discountIR))
print("You pay to the Union {} reais. \n".format(discountSind))
print("With the discounts, your net salary is: ", netSalary)