def dfs(conn_list, start):
	used = []
	chain = []

	print('start: {}'.format(start))

	def __dfs(v):
		chain.append(v)

		if conn_list[v - 1] is None:
			return

		try:
			for _v in conn_list[v - 1]:
				if conn_list[v - 1] is None:
					return
				if _v not in used:

					if _v == start:
						print('{} -> {}'.format(v, _v))
						print('chain: {}'.format(chain))
						print('found cycle!')

						shrink(conn_list, start, chain)

						print('shrinked:')
						pretty(conn_list)
						print()

						dfs(conn_list, start)

						return
					else:
						print('{} -> {}'.format(v, _v))

						used.append(_v)
						__dfs(_v)
						chain.remove(_v)
						pass
		except RuntimeError:
			return
		pass

	__dfs(start)

	print('end.')


def shrink(conn_list, start, chain):
	print('shrink: {}'.format(chain))

	if start in chain:
		chain.remove(start)

	for _v in chain:
		union = set.union(conn_list[start - 1], conn_list[_v - 1])
		union.remove(_v)

		print('{} + {} = {}'.format(start, _v, union))

		conn_list[start - 1] = union

		for vert_set in conn_list:
			if vert_set is not None:
				if _v in vert_set:
					vert_set.remove(_v)
					vert_set.add(start)

		conn_list[_v - 1] = None

	if start in conn_list[start - 1]:
		conn_list[start - 1].remove(start)


def invert(conn_list):
	size = range(len(conn_list))
	conn_list_t = [set() for i in size]

	for i in size:
		if conn_list[i] is not None:
			for v in conn_list[i]:
				conn_list_t[v - 1].add(i + 1)
		else:
			conn_list_t[i] = None

	return conn_list_t


def single_connectivity(conn_list):
	count = 0
	for i in range(len(conn_list)):
		if conn_list[i] is None:
			count += 1
	return count == (len(conn_list) - 1)


def ins(conn_list):
	return outs(invert(conn_list))


def outs(conn_list):
	count = 0
	if single_connectivity(conn_list):
		return 0
	for i in range(len(conn_list)):
		if conn_list[i] is not None:
			if len(conn_list[i]) == 0:
				count += 1
	return count


def pretty(m):
	c = 1
	for x in m:
		print('{}:'.format(c), end=' ')
		c += 1
		if x is None:
			print('None')
		else:
			for y in x:
				print(y, end=' ')
			print()
	print()


def main():
	with open('input.txt', mode='r') as file:
		size = int(file.readline())
		connectivity = []
		for i in range(size):
			links = set(int(word) for word in file.readline().split(' '))
			links.remove(0)
			connectivity.append(links)

	pretty(connectivity)

	for i in range(size):
		if connectivity[i] is not None:
			dfs(connectivity, i + 1)

	i = ins(connectivity)
	o = outs(connectivity)

	answer = '{}\n{}'.format(max(1, i), max(o, i))

	print('\nreversed:')
	pretty(invert(connectivity))

	print('\n------------------------------\n')
	print('shrinked:')
	pretty(connectivity)
	print('------------------------------\n')

	print('answer:\n{}'.format(answer))

	with open('output.txt', mode='w+') as file:
		file.write(answer)
	pass


if __name__ == '__main__':
	main()
