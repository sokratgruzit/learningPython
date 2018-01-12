"""

Calculating type of the year

"""

year = int(input())
if 1900 <= year <= 3000:
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		print('Високосный')
	else:
		print('Обычный')
else:
	print('Введи год в нужном диапазоне и не тупи')