def is_open_0(h,m):
	if h>=8 and h<17:
		print('YES')
	else:
		print('NO')

def is_open(h,m):
	if h>=8 and h<=17:
		if h==17 and m!=0:
			print('NO')
		else:
			print('YES')
	else:
		print('NO')

