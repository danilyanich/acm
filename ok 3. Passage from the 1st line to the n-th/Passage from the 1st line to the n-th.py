def find_min(array, r):
	return min(array[max(0, r): min(r + 3, len(array))])


if __name__ == '__main__':
	with open('input.txt', mode='r') as file:
		y, x = [int(s) for s in file.readline().split()]
		matrix = [[int(s) for s in file.readline().split()] for j in range(y)]

	for i in reversed(range(y - 1)):
		for j in range(x):
			matrix[i][j] = find_min(matrix[i + 1], j - 1) + matrix[i][j]

	penalty = min(matrix[0])

	for r in matrix:
		print(r)

	with open('output.txt', mode='w+') as file:
		file.write(str(penalty))
	pass
