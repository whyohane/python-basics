'''18. Write a program that asks for the size of a downloadable file (in MB) and the speed of an Internet link (in Mbps),
Calculate and report the approximate file download time using this link (in minutes). '''

file = float(input("Enter the size of a file to download in MEGABYTES: \n"))

bits = file * 8.388608

internet = float(input("Enter your internet speed in MEGABITS PER SECOND: \n"))

time = bits / internet

minutes = time / 60

print("To download the file of size {} MEGABYTES took {} minutes. \n".format(file, minutes))