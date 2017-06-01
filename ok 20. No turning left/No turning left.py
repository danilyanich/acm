def dfs(conn_list, _from, _to, info, came):
	used = []
	chain = []

	print('start: {}'.format(_from))

	def __dfs(v, p, depth):
		used.append((p, v))
		chain.append(v)

		d = ('{:>' + str(2 * depth) + '}').format('')

		for _v in conn_list[v - 1]:
			if _v != p and (v, _v) not in used:
				if not on_left(info[p - 1], info[v - 1], info[_v - 1]):

					print(d + '{} -> {}'.format(v, _v))

					if _v == _to:
						chain.append(_to)
						return False

					if not __dfs(_v, v, depth + 1):
						return False

					chain.remove(_v)
				else:
					print(d + '{} forbidden. parent={} current={}'.format(_v, p,
																		  v))

		return True

	__dfs(_from, came, 0)

	print('end.')

	return chain


def on_left(a, b, m):
	x1, y1 = a
	x2, y2 = b
	x3, y3 = m
	det = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)
	return det < 0


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
		crosses, roads = [int(w) for w in file.readline().split()]

		graph = [[] for i in range(crosses)]
		info = [None for i in range(crosses)]

		for i in range(roads):
			x1, y1, x2, y2, c1, c2 = [int(w) for w in file.readline().split()]
			if not info[c1 - 1]:
				info[c1 - 1] = (x1, y1)
			if not info[c2 - 1]:
				info[c2 - 1] = (x2, y2)
			graph[c1 - 1].append(c2)
			graph[c2 - 1].append(c1)

		_from, _to = [int(w) for w in file.readline().split()]

	c_from = info[_from - 1]
	c_came = (c_from[0], c_from[1] - 1)

	if c_came not in info:
		info.append(c_came)

	pretty(graph)
	pretty(info)

	chain = dfs(graph, _from, _to, info, info.index(c_came) + 1)
	str_chain = ' '.join(map(str, chain))
	answer = 'Yes\n{}'.format(str_chain) if len(chain) > 1 else 'No'

	with open('output.txt', mode='w+') as file:
		file.write('{}'.format(answer))


if __name__ == '__main__':
	main()
