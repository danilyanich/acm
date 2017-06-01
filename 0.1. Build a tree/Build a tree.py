class Vertex:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert_it(root, key):
	parent = None
	vert = root
	while vert is not None:
		parent = vert
		if key < vert.key:
			vert = vert.left
		elif key > vert.key:
			vert = vert.right
		else:  # thee already has same key
			return root

	new_vert = Vertex(key)

	if parent is None:
		root = new_vert
	elif key < parent.key:
		parent.left = new_vert
	elif key > parent.key:
		parent.right = new_vert

	return root


def iteration(root, consumer):
	if root is not None:
		consumer(root.key)
		iteration(root.left, consumer)
		iteration(root.right, consumer)


if __name__ == '__main__':
	tree = None
	with open('input.txt', mode='r') as file:
		for line in file.readlines():
			tree = insert_it(tree, int(line))

	with open('output.txt', mode='w+') as file:
		iteration(tree, lambda x: file.write('{}\n'.format(x)))
