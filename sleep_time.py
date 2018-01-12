"""

Calculating the optimal time for sleep

"""

A = int(input())
B = int(input())
H = int(input())
if H <= B and H >= A:
	print('Это нормально')
elif H <= A and H <= B and A <= B:
	print('Недосып')
elif H >= A and H >= B and A <= B:
	print('Пересып')
else:
	print('Некорректные данные')