#!/bin/python3
import random

def game():
	list_of_funcs = ["oct", "bin", "hex"]
	for i in range(100):
		number = random.randint(1,100000000)
		converted_number = eval(list_of_funcs[random.randint(0,2)])(number)
		print(converted_number)

		got_from_user = input()

		if str(got_from_user) != str(number):
			print("meh~")
			exit(0)

	with open('flag.txt') as f:
		flag = f.readlines()[0]
		print(flag)

print("Wanna play my game?\n\nWell, rules are pretty easy:\nConvert all these values to decimal, that's just it")
user_input = input("Wanna play my game? <Y/N> ")
while True:
	if user_input in "Yy":
		game()
	elif user_input in "Nn":
		print("it's such a pity... bye bye...")
		exit(0)
	else:
		user_input = input("Wanna play my game? <Y/N> ")
