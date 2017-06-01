matrix = None
mod = 1000000009

if __name__ == '__main__':
	with open('input.txt', mode='r') as file:
		n, k = map(int, file.readline().split())

	size = max(n, k) + 1
	matrix = [[0 for j in range(size - i)] for i in range(size)]

	matrix[0][0] = 1
	for diag in range(1, size):
		matrix[diag][0], matrix[0][diag] = 1, 1
		for elem in range(1, diag):
			i, j = diag - elem, elem
			matrix[i][j] = (matrix[i - 1][j] + matrix[i][j - 1]) % mod


	def _c(_k, _n):
		if 0 <= _k <= _n < len(matrix):
			i, j = _n - _k, _k
			return matrix[i][j]
		return 0


	cases = 0

	for n in range(1, size):
		for k in range(1, n + 1):
			print('C{}/{} = {:<15}'.format(k, n, _c(k, n)), end=' ')
		print()

	print('stairs: 0', end='')

	stair_cases = 0
	for p in range(1, 2 * k + 1):
		stair_cases = (_c(p, k) + stair_cases) % mod

		print(' + C{}/{}'.format(p, k), end='')

	print('  x2 = {}'.format(stair_cases))
	print('lifts: 0', end='')

	lifts = 0
	for p in range(0, n + 1):
		lifts = (_c(p, n) + lifts) % mod
		print(' + C{}/{}'.format(p, n), end='')

	print(' = {}'.format(lifts))

	cases = (lifts + stair_cases) % mod

	with open('output.txt', mode='w+') as file:
		file.write('{}'.format(cases))
