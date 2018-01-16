for k in range(2):
    a = int(input('Введите чиcло от 1 до 9 '))
    while (0 > a) or (a > 10):
        a = int(input('Введите чиcло от 1 до 9 '))
    b = int(input('Введите число >= ' + str(a)))
    while a > b:
        b = int(input('Введите число >= ' + str(a)))
    if k == 0:
        rows = [x for x in range(a, b + 1)]
    else:
        cols = [x for x in range(a, b + 1)]
table = [[' '] + cols]
for i in range(rows[0], rows[-1] + 1):
	line = [i]
	for j in range(cols[0], cols[-1] + 1):
		row = i * j
		line.append(row)
	table.append(line)
for line in table:
  print('\t'.join([str(n) for n in line]))