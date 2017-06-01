class Vertex:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.min_height = 0


def insert_rec(root, key):
	if root is None:
		return Vertex(key)
	elif key < root.key:
		root.left = insert_rec(root.left, key)
	elif key > root.key:
		root.right = insert_rec(root.right, key)
	return root


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


def delete_rec(root, key):
	if root is not None:
		if key > root.key:
			root.right = delete_rec(root.right, key)
			return root
		elif key < root.key:
			root.left = delete_rec(root.left, key)
			return root
		# root.key == key
		if root.right is None:
			return root.left
		elif root.left is None:
			return root.right
		# root has left and right branches
		max_key = maximum(root.left)
		root.key = max_key
		root.left = delete_rec(root.left, max_key)
	return root


def maximum(root):
	if root.right is not None:
		return maximum(root.right)
	return root.key


def delete_it(root, key):
	parent = None
	vert = root

	while True:
		if vert is None:
			return root
		if key < vert.key:
			parent = vert
			vert = vert.left
		elif key > vert.key:
			parent = vert
			vert = vert.right
		else:  # found vertex
			break

	result = None

	if vert.left is None:
		result = vert.right
	elif vert.right is None:
		result = vert.left
	else:
		max_node_parent = vert
		max_node = vert.left
		while max_node.right is not None:
			max_node_parent = max_node
			max_node = max_node.right

		result = vert
		vert.key = max_node.key
		replace_child(max_node_parent, max_node, max_node.left)

	replace_child(parent, vert, result)
	return root


def replace_child(parent, old, new):
	if parent is None:
		tree.root = new
	elif parent.left == old:
		parent.left = new
	elif parent.right == old:
		parent.right = new


def straight_left_iteration(root, consumer):
	if root is not None:
		consumer(root)
		straight_left_iteration(root.left, consumer)
		straight_left_iteration(root.right, consumer)


def iteration(root, consumer):
	if root is not None:
		consumer(root)
		iteration(root.left, consumer)
		iteration(root.right, consumer)


def map_height(root):
	if root is not None:
		left_height = map_height(root.left)
		right_height = map_height(root.right)
		if root.left is None or root.right is None:
			height = max(left_height, right_height)
		else:
			height = min(left_height, right_height)
		root.min_height = height
		return root.min_height + 1
	return 1


min_height = None
middle_vertex = None
vertex_list = []


def check_on_min_path(root, depth, on_left, on_right):
	if root is not None:
		check_on_min_path(root.left, depth + 1, on_left, on_right + 1)

		left_height = root.left.min_height if root.left is not None else 0
		right_height = root.right.min_height if root.right is not None else 0

		def info():
			f = '{:<5} left: {:<5} right: {:<5} depth: {:<5} on_left: {:<5} on_right: {:<5}'
			print(f.format(root.key, left_height, right_height, depth, on_left,
						   on_right))

		if root.left is None and root.right is not None:
			if right_height + depth == min_height:

				info()

				if on_left + 1 == middle_vertex:
					vertex_list.append(root.key)

					print('YES case: left')

		elif root.right is None and root.left is not None:
			if left_height + depth == min_height:

				info()

				if on_right + 1 == middle_vertex:
					vertex_list.append(root.key)

					print('YES case: right')

		elif root.right is not None and root.left is not None:
			height = min(left_height, right_height)
			if height + depth == min_height:

				info()

				if left_height < right_height:
					if on_right + 1 == middle_vertex:
						vertex_list.append(root.key)

						print('YES case: right')

				elif left_height > right_height:
					if on_left + 1 == middle_vertex:
						vertex_list.append(root.key)

						print('YES case: left')

				elif left_height == right_height:
					if on_left + 1 == middle_vertex or on_right + 1 == middle_vertex:
						vertex_list.append(root.key)

						print('YES case: left or right')

		else:
			if depth == min_height:

				info()

				if on_right + 1 == middle_vertex or on_left + 1 == middle_vertex:
					vertex_list.append(root.key)

					print('YES case: left right')

		check_on_min_path(root.right, depth + 1, on_left + 1, on_right)


if __name__ == '__main__':
	tree = None
	with open('tst.in', mode='r') as file:
		floats = [int(line) for line in file.readlines()]
		for f in floats:
			tree = insert_it(tree, f)

	map_height(tree)
	min_height = tree.min_height
	middle_vertex = int((min_height + 1) / 2)

	if min_height % 2 != 0:
		check_on_min_path(tree, 1, 0, 0)

	print(vertex_list)

	for vertex in vertex_list:
		tree = delete_it(tree, vertex)

	with open('tst.out', mode='w+') as file:
		straight_left_iteration(tree, lambda root: file.write(
			'{}\n'.format(root.key)))
	pass
