'''11. Write a Program that asks for 2 integers and a real number. Calculate and show:
1- the product of twice the first and half the second.
2- the sum of three times the first and third.
3- the third raised to the cube.'''

int1 = int(input("Enter the first integer number: \n"))
int2 = int(input("Enter the second integer number: \n"))
real = float(input("Enter a real number: \n"))

product = (int1 * 2) * (int2 / 2)
sum = (int1 * 3) + real
raised = real**3

print("The product of twice the first and half the second: ", product)
print("The sum of the triple of the first and the third: ", sum)
print("The third cubed: ", raised)