def dfs(conn_list, start):
	used = []
	chain = []

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
						shrink(conn_list, start, chain)
						dfs(conn_list, start)
						return
					else:
						used.append(_v)
						__dfs(_v)
						chain.remove(_v)
						pass
		except RuntimeError:
			return
		pass

	__dfs(start)


def shrink(conn_list, start, chain):
	if start in chain:
		chain.remove(start)

	for _v in chain:
		union = set.union(conn_list[start - 1], conn_list[_v - 1])
		union.remove(_v)

		conn_list[start - 1] = union

		for vert_set in conn_list:
			if vert_set is not None:
				if _v in vert_set:
					vert_set.remove(_v)
					vert_set.add(start)

		conn_list[_v - 1] = None

	if start in conn_list[start - 1]:
		conn_list[start - 1].remove(start)


def single_connectivity(conn_list):
	count = 0
	for i in range(len(conn_list)):
		if conn_list[i] is None:
			count += 1
	return count == (len(conn_list) - 1)


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
	with open('input.in', mode='r') as file:
		size = int(file.readline())
		conn_list = [set() for j in range(size)]
		for j in range(size):
			i = 1
			for e in file.readline().split():
				if int(e) == 1:
					conn_list[j].add(i)
				i += 1

	for i in range(size):
		if conn_list[i] is not None:
			dfs(conn_list, i + 1)

	pretty(conn_list)

	answer = '{}'.format('YES' if single_connectivity(conn_list) else 'NO')

	with open('output.out', mode='w+') as file:
		file.write(answer)
	pass


if __name__ == '__main__':
	main()
