class Vertex:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# recursive
def insert_rec(root, key):
	if root is None:
		return Vertex(key)
	elif key < root.key:
		root.left = insert_rec(root.left, key)
	elif key > root.key:
		root.right = insert_rec(root.right, key)
	return root


# left, recursive
def delete_left_rec(root, key):
	if root is not None:
		if key > root.key:
			root.right = delete_left_rec(root.right, key)
			return root
		elif key < root.key:
			root.left = delete_left_rec(root.left, key)
			return root
		# root.key == key
		if root.right is None:
			return root.left
		elif root.left is None:
			return root.right
		# root has left and right branches
		max_key = maximum(root.left)
		root.key = max_key
		root.left = delete_left_rec(root.left, max_key)
	return root


def maximum(root):
	if root.right is not None:
		return maximum(root.right)
	return root.key


def minimum(root):
	if root.left is not None:
		return minimum(root.left)
	return root.key


# template for all iterations
def iteration(root, consumer):
	if root is not None:
		iteration(root.left, consumer)
		consumer(str(root.key))
		iteration(root.right, consumer)


def elapsed(function, *args):
	function(args)


if __name__ == '__main__':
	exit()
