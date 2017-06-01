def spawn_binomial_coefs(n):
	size = n + 1
	matrix = [[0 for j in range(size - i)] for i in range(size)]
	matrix[0][0] = 1

	for diag in range(1, size):
		matrix[diag][0], matrix[0][diag] = 1, 1
		for elem in range(1, diag):
			i, j = diag - elem, elem
			matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

	def __c(_k, _n):
		if 0 <= _k <= _n < len(matrix):
			i, j = _n - _k, _k
			return matrix[i][j]
		return 0

	return __c


def max_2_deg(number):
	count = 0
	while number > 1:
		number >>= 1
		count += 1
	return count


def numbers_fit(number, ones, __c):
	it_deg = max_2_deg(number)
	it, fit, met = 1, 0, 0

	for i in range(it_deg):
		it <<= 1

	while it_deg >= 0:

		if it & number:
			met += 1
			k, n = ones - met + 1, it_deg

			print('1 n: {} k: {}'.format(n, k), end='')

			if 0 <= k <= n:
				c = __c(k, n)
				fit += c

				print(' C{}/{} = {}'.format(k, n, c), end='')

			print()

		else:
			print('0')

		it_deg -= 1
		it >>= 1

	if met == ones:
		fit += 1
		print('+1')

	print()

	return fit


def bits(number):
	count = 0
	while number:
		if number & 1:
			count += 1
		number >>= 1
	return count


def main():
	with open('input.txt', mode='r') as file:
		A, B, ones = [int(w) for w in file.readline().split()]

	size = max_2_deg(B)
	binomial = spawn_binomial_coefs(size)

	print('{:b}'.format(A))
	print('{:b}\n'.format(B))

	if A != B:
		fits = numbers_fit(B, ones, binomial) - numbers_fit(A - 1, ones, binomial)
	else:
		b = bits(B)
		fits = b if b == ones else 0

	with open('output.txt', mode='w+') as file:
		file.write('{}'.format(fits))
	pass


if __name__ == '__main__':
	main()