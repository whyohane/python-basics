"4. Make a program that asks for the 4 bimonthly grades and shows the average."

print("# The Program that shows the average of 4 grades! #\n")

sum = 0

for i in range (4):

    x = float(input("Enter the {} grade: ".format(i+1)))
    sum = sum + x

average = sum/4

print("The average is: ", average)