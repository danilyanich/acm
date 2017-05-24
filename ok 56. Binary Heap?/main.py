import math

if __name__ == '__main__':
	size = None
	data = []
	with open('input.txt', mode='r') as file:
		size = int(file.readline())
		data.append(0)
		data += [int(var) for var in file.readline().split(' ')]
	isHeap = True
	for i in range(1, math.ceil(size / 2) + 1):
		l, r = 2 * i, 2 * i + 1
		if (l <= size and data[i] > data[l]) or (r <= size and data[i] > data[r]):
			isHeap = False
			break
	with open('output.txt', mode='w+') as file:
		file.write('{}'.format('Yes' if isHeap else 'No'))
	pass
