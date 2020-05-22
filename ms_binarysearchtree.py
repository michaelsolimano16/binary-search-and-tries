# Michael Solimano 2020
# Practice implementing a binary search tree class

class Node():
	#create a basic node object:

	def __init__(self, val=None):
		#Constructor for node objects giving them a data value and children pointers.
		#Here, there can only be two children. If more were allowed, I would probably use a 
		#list instead of pointers.

		self.data = val
		self.lchild = None
		self.rchild = None

class bstTree():
	#create a BST, where duplicates are not allowed and each node has a max of two children

	def __init__(self):
		#The bst tree begins with a root.
		self.root = None

	def isEmpty(self):
		#Check if the tree is empty
		if self.root == None:
			return True
		else:
			return False

	def add_node(self, val):
		#add a node to the tree

		new_node = Node(val)

		#Check if the tree is empty. If so, make new node the root.
		if self.isEmpty() == True:
			self.root = new_node
			return

		spotter = True
		node_tracker = self.root

		#Move through the tree until we find the proper position for new node
		#When we find this spot, 'spotter' is set to False and we break from the loop
		while spotter:
			if new_node.data == node_tracker.data:
				print("This value is already in the tree.")
				return
			elif new_node.data < node_tracker.data:
				if node_tracker.lchild == None:
					node_tracker.lchild = new_node
					print(f"Adding {val} as left child.")
					spotter = False
				else:
					node_tracker = node_tracker.lchild
			else:
				if node_tracker.rchild == None:
					node_tracker.rchild = new_node
					print(f"Adding {val} as right child.")
					spotter = False
				else:
					node_tracker = node_tracker.rchild

	def inOrderTraversal(self, current_node):
		#Traverse the tree in order of data values.
		#The root should be passed as arg
		if current_node != None:
			#Go all the way down the left side recursively before printing node
			self.inOrderTraverse(current_node.lchild)

			#Once that's done, we can print the current node
			print(f"Visited {current_node.data}.")

			#With the current node printed, go down the right for all values greater
			self.inOrderTraverse(current_node.rchild)

	
	def preOrderTraversal(self, current_node):
		#A traversal printing nodes top-down, where root is the first node visited.

		if current_node != None:
			print(f"Visited {current_node.data}!")
			self.preOrderTraversal(current_node.lchild)
			self.preOrderTraversal(current_node.rchild)

	def postOrderTraversal(self, current_node):
		#Recursively print the tree visiting children before the current node is printed
		#This is a more or less bottom-up print, where the root is last node visited.

		if current_node != None:
			self.postOrderTraversal(current_node.lchild)
			self.postOrderTraversal(current_node.rchild)
			print(f"Visited {current_node.data}.")


tree = bstTree()
tree.add_node(10)
tree.add_node(2)
tree.add_node(20)
tree.add_node(1)
tree.preOrderTraversal(tree.root)
