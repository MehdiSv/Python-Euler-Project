n = 100

def factorial(number):
	if number == 1:
		return 1
	res = number * factorial(number - 1)
	return res

res = factorial(n)

print reduce(lambda x, y: x + y, [int(i) for i in str(res)])