
if __name__ == '__main__':
	size = int
	with open('input.txt', mode='r') as file:
		size = int(file.readline())
	deg = 0
	with open('output.txt', mode='w+') as file:
		while size != 0:
			if size & 1 == 1:
				file.write(str(deg) + '\n')
			deg += 1
			size >>= 1
	pass
