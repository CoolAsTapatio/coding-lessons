def highest_numbers(num1, num2, num3, num4, num5):
# def represents the funtion and parameters
	high_number = max(num1,num2,num3,num4, num5)
	if num5 > num4 and num5 > num3 and num5 > num2 and num5 > num1:
		print(str(num5) + ' is the bigesst parameter' )
# the if represents num5 being the greatest value
	elif num4 > num5 and num4 > num3 and num4 > num2 and num4 > num1:
		print(str(num4) + ' is the bigesst parameter' )
# the if represents num4 being the greatest value
	elif num3 > num5 and num3 > num4 and num3 > num2 and num3 > num1:
				print(str(num3) + ' is the bigesst parameter' )
# the if represents num3 being the greatest value	
	elif num2 > num5 and num2 > num4 and num2 > num3 and num2 > num1:
				print(str(num2) + ' is the bigesst parameter' )
# the if represents num2 being the greatest value
	elif num1 > num5 and num1 > num4 and num1 > num3 and num1 > num2:
				print(str(num1) + ' is the bigesst parameter' )
	if num5 == num4 == num3 == num2 == num1:
		print('the parameters are all the same value')
# the if represents num1 being the greatest value
	
# the print statment represents wand the function prints out not including parameters

# the if statments dtermine the scond highest value
	if not (num1 == num2 == num3 == num4 == num5):
		if num5 == high_number:	
			second_highest_number = max(num4, num3, num2, num1)
			print(str(second_highest_number) + ' is th second highest value')
			print(str(high_number + second_highest_number) + ' is the sum of the 2 highest numbers')
		if num4 == high_number:	
			second_highest_number = max(num5, num3, num2, num1)
			print(str(second_highest_number) + ' is th second highest value')
			print(str(high_number + second_highest_number) + ' is the sum of the 2 highest numbers')
		if num3 == high_number:	
			second_highest_number == max(num4, num5, num2, num1)
			print(str(second_highest_number) + ' is th second highest value')
			print(str(high_number + second_highest_number) + ' is the sum of the 2 highest numbers')
		if num2 == high_number:	
			second_highest_number == max(num4, num3, num5, num1)
			print(str(second_highest_number) + ' is th second highest value')
			print(str(high_number + second_highest_number) + ' is the sum of the 2 highest numbers')
		if num1 == high_number:	
			second_highest_number = max(num4, num3, num2, num5)
			print(str(second_highest_number) + ' is th second highest value')
			print(str(high_number + second_highest_number) + ' is the sum of the 2 highest numbers')
# the print represents the sum of the 2 highest numbers.	
	



	
if __name__ == "__main__":
	highest_numbers(18, 9, 9, 9, 9)
	print('\n')
	highest_numbers(2, 4, 6, 8, 10)
	print('\n')
	highest_numbers(1, 5, 3, 14, 9)
	