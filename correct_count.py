"""

Counting programmers in the class correctly

"""

i = int(input())
endings = [' программист', ' программиста', ' программистов']
if 0 <= i <= 1000:
	if 5 <= i%10 <= 9 or 5 <= i%100 <= 19 or i == 0 or i%100 == 0 or i%10 ==0:
		print(str(i) + endings[2])
	elif 2 <= i%10 <= 4:
		print(str(i) + endings[1])
	elif i%10 and i%100 == 1:
		print(str(i) + endings[0])
	else:
		print(str(i) + endings[0])
else:
	print('Можно вводить числа от 0 и до 1000 влючительно')