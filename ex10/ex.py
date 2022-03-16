def native_mul(x,y):
	r = x
	if y == 0:
		return 0
	for i in range(0, y - 1):
		x = x+r
	return x

def ex9():
	for i in range(10):
		for j in range(10):
			assert ((i*j) == native_mul(i, j))
	print('Done!')


def fast_mul(x,y):
	res = 0
	if x % 2 == 1:
		res = y
	if x == 0 or y == 0:
		return 0
	ll = x // 2
	for i in range(ll):
		x = x // 2; y = y * 2
		if x % 2 == 1:
			res += y
	return res

def fast_pow(x, y):
	m = x
	t = 1
	while y:
		if y % 2:
			t *= m
		m *= m
		y //= 2
	return t



def ex10():
	for i in range(10):
		for j in range(10):
			assert ((i*j) == fast_mul(i, j))
	print('Done!')
	for i in range(10):
		for j in range(10):
			assert ((i**j) == fast_pow(i, j))
	print('Done!')

def main():
	ex9()
	ex10()

main()