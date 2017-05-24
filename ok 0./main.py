if __name__ == '__main__':
	number_set = set()
	with open('input.txt', mode='r') as file:
			for line in file:
				number_set.add(int(line))
	result = sum(number_set)
	with open('output.txt', mode='w+') as file:
		file.write(str(result))
