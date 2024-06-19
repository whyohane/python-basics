'''13. Taking a person's height (h) as input, build an algorithm that calculates their ideal weight, using the following formulas:
1- For men: (72.7*h) - 58
2- For women: (62.1*h) - 44.7'''

print("# The ideal weight of men and women! #\n")

height = float(input("Enter your height: "))
gen = input("Enter your gender: man ou woman: \n")
if gen == 'man' :
    weightM = (72.7*height) - 58
    print("O seu peso ideal é: ", weightM)
else :
        weightW = (62.1*height) - 44.7 
        print("Your ideal height is: ", weightW)