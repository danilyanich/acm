import sys


class Pair:
	def __init__(self, x, y):
		self.y = y
		self.x = x


if __name__ == '__main__':
	size = None
	data = []
	with open('input.txt', mode='r') as file:
		size = int(file.readline())
		for i in range(size):
			ints = [int(var) for var in file.readline().split(' ')]
			matrix = Pair(ints[0], ints[1])
			data.append(matrix)

	values = [[0 for i in range(size)] for j in range(size)]

	for i in range(1, size):
		for j in range(0, size - i):
			x, y = j, j + i
			values[x][y] = sys.maxsize
			values[x][y] = min([values[x][k] + values[k + 1][y] + data[x].x * data[k].y * data[y].y for k in range(x, y)])

	with open('output.txt', mode='w+') as file:
		file.write(str(values[0][size - 1]))
	pass
