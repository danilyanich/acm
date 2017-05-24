import random
import timeit


class Vertex:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert_iter(root, key):
	if root in None:
		return Vertex(key)


def insert_rec(root, key):
	if root is None:
		return Vertex(key)
	elif key < root.key:
		root.left = insert_rec(root.left, key)
	elif key > root.key:
		root.right = insert_rec(root.right, key)
	return root


def iteration(root, consumer):
	if root is not None:
		iteration(root.left, consumer)
		consumer(root.key)
		iteration(root.right, consumer)


if __name__ == '__main__':
	start = timeit.default_timer()
	'''with open('input.txt', mode='w+') as file:
		for i in range(1, 100000):
			file.write(str(random.randrange(-i, i)) + '\n')
	print('elapsed:' + str(timeit.default_timer() - start))'''

	start = timeit.default_timer()
	tree = None
	with open('input.txt', mode='r') as file:
		for line in file.readlines():
			tree = insert_rec(tree, int(line))
	print('elapsed:' + str(timeit.default_timer() - start))

	start = timeit.default_timer()
	with open('output.txt', mode='w+') as file:
		iteration(tree, lambda x: file.write('{}\n'.format(x)))
	print('elapsed:' + str(timeit.default_timer() - start))
