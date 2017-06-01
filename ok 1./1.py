class Vertex:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.descendants = 0


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
		min_key = minimum(root.right)
		root.key = min_key
		root.right = delete_rec(root.right, min_key)
	return root


def minimum(root):
	if root.left is not None:
		return minimum(root.left)
	return root.key


def straight_left_iteration(root, consumer):
	if root is not None:
		consumer(root)
		straight_left_iteration(root.left, consumer)
		straight_left_iteration(root.right, consumer)


def find_approachable(root, trailing_list):
	if root is not None:
		find_approachable(root.left, trailing_list)

		left_desc = root.left.descendants if root.left is not None else 0
		right_desc = root.right.descendants if root.right is not None else 0

		if right_desc != left_desc:
			trailing_list.append(root.key)

		find_approachable(root.right, trailing_list)
	return trailing_list


def map_descendants(root):
	if root is not None:
		left_desc = map_descendants(root.left)
		right_desc = map_descendants(root.right)
		root.descendants = left_desc + right_desc + 1
		return root.descendants
	return 0


if __name__ == '__main__':
	tree = None
	with open('in.txt', mode='r') as file:
		floats = [int(line) for line in file.readlines()]
		for f in floats:
			tree = insert_rec(tree, f)

	map_descendants(tree)
	approachable = find_approachable(tree, [])

	if len(approachable) % 2 != 0:
		key = approachable[int(len(approachable) / 2)]
		tree = delete_rec(tree, key)

	with open('out.txt', mode='w+') as file:
		straight_left_iteration(tree, lambda root: file.write(
			'{}\n'.format(root.key)))
	pass
