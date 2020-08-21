#打印1至100的数字，如果碰到含7的数，或者7的倍数，就跳过这个数
for num in range(1,101):
	if num % 7 == 0:
		continue
	elif num // 10 == 7:
		continue
	elif num % 10 == 7:
		continue
	else:
		print(num)
