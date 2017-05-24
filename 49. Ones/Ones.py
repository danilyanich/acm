import re

размер = int()
матрица = list()


def биномиальный(n, k):
	i = n - k
	j = k
	if 0 <= i < размер and 0 <= j < размер:
		return матрица[i][j]
	return 0


def чисел(число, битов):
	коэффициент = 0
	плавающая_единица = 1
	степень = битов - 1
	for r in range(степень):
		плавающая_единица <<= 1
	единиц = 0

	while плавающая_единица:
		if число & плавающая_единица:
			единиц += 1
			коэффициент += биномиальный(степень, K - единиц + 1)
			print(1, end=' ')
			print('C{}/{} = {}'.format(K - единиц + 1, степень, биномиальный(степень, K - единиц + 1)))
		else:
			print(0)
		плавающая_единица >>= 1
		битов -= 1
		степень -= 1

	print()
	return коэффициент


def битов(число):
	количество = 0
	while число != 0:
		количество += 1
		число >>= 1
	return количество


if __name__ == '__main__':

	with open('input.txt', mode='r') as file:
		A, B, K = [int(word) for word in re.split(r'\s+', file.readline())]

	размер = битов(B) + 1
	матрица = [[0 for x in range(размер)] for y in range(размер)]

	матрица[0][0] = 1
	for d in range(1, размер):
		матрица[d][0], матрица[0][d] = 1, 1
		for e in range(1, d):
			i, j = d - e, e
			матрица[i][j] = матрица[i - 1][j] + матрица[i][j - 1]

	print(str(bin(A)).replace('0b', ''))
	print(str(bin(B)).replace('0b', ''))
	print()

	A = max(0, A - 1)
	искомый = чисел(B, битов(B)) - чисел(A, битов(A))

	print('числа:')
	искомый1 = 0
	for x in range(A, B + 1):
		ones = 0
		y = x
		while x:
			if x & 1:
				ones += 1
			x >>= 1
		if ones == K:
			print(str(bin(y)).replace('0b', ''))
			искомый1 += 1

	print()
	print(искомый)
	print(искомый1)
	print(искомый1 == искомый)

	with open('output.txt', mode='w+') as file:
		file.write(str(искомый))
	pass
