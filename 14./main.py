import math


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
	return 0


min_height = None
middle_vertex = None
vertex_list = []


def check_on_min_path(root, depth, on_left, on_right):
	if root is not None:
		check_on_min_path(root.left, depth + 1, on_left, on_right + 1)
		if depth + root.min_height == min_height:
			if on_left + 1 == middle_vertex or on_right + 1 == middle_vertex:
				vertex_list.append(root.key)
		check_on_min_path(root.right, depth + 1, on_left + 1, on_right)
		return root.min_height
	return 0


if __name__ == '__main__':
	tree = None
	with open('tst.in', mode='r') as file:
		floats = [int(line) for line in file.readlines()]
		for f in floats:
			tree = insert_rec(tree, f)

	map_height(tree)
	min_height = tree.min_height
	middle_vertex = math.ceil((min_height + 1) / 2)

	print('mh={}; hh={};'.format(min_height, middle_vertex))

	if min_height % 2 == 0:
		check_on_min_path(tree, 0, 0, 0)

	print(vertex_list)

	for vertex in vertex_list:
		tree = delete_rec(tree, vertex)

	with open('tst.out', mode='w+') as file:
		iteration(tree, lambda root: file.write(
			'{}\n'.format(root.key)))
	pass
