pushes = [
	lambda x, y: (x, y + 1),
	lambda x, y: (x + 1, y + 1),
	lambda x, y: (x + 1, y),
	lambda x, y: (x + 1, y - 1),
	lambda x, y: (x, y - 1),
	lambda x, y: (x - 1, y - 1),
	lambda x, y: (x - 1, y),
	lambda x, y: (x - 1, y + 1)
]

cache = {(0, 0)}


def main():
	x, y = 0, 0
	answer = 'No'
	with open('in.txt', mode='r') as file:
		states = int(file.readline())
		for step in [int(w) for w in file.readline().split()]:
			x, y = pushes[step](x, y)
			if (x, y) not in cache:
				cache.add((x, y))
			else:
				answer = 'Yes'
				break

	with open('out.txt', mode='w+') as file:
		file.write('{}'.format(answer))


if __name__ == '__main__':
	main()
