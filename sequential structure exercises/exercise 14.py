'''João, a good man, bought a microcomputer to control his daily work output. 
Every time he brings a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos) he must pay a fine of
R$4.00 per excess kilo. João needs you to write a program that reads the weight variable (fish weight) and calculates the excess.
Record in the excess variable the number of kilos beyond the limit and in the fine variable the amount of the fine that João must pay.
Print program data with appropriate messages.'''

print("# Program to calculate excess fish and fine applied! #\n")

print("The maximum weight is 50KG. Each excess kg costs R$4.00. \n")

fish = float(input("Enter the value of today: "))
excess = fish - 50

if excess > 0 :
    fine = excess * 4
    print("Overweight! Fine in the amount of: R$", fine)
else :
    print("The weight is within the limits established by the regulations.")