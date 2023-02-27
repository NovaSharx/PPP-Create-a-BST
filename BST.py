# Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.nodes = []

    def __str__(self):
        return (f"{self.data}")

    def __repr__(self):
        return (f"{self.data}")


node1 = BSTNode(3)
print(node1)  # 3

node2 = BSTNode(4, left=node1)
print(node2)  # 4

node3 = BSTNode()
print(node3)  # None
node3.data = 5
print(node3)  # 5


# Part 2: Create a BST class
# Part 3: Add functionality to your BST class

class BST:
    def __init__(self, root=None):
        self.root = root
        self.contents = []
        if self.root is not None:
            self.contents = [root.data]

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
            self.print_tree(node.left, level + 1)

    def __str__(self):
        if self.root is None:
            return "The tree is empty"
        else:
            self.output = ''
            self.print_tree(self.root)
            return self.output

    def __repr__(self):
        if self.root is None:
            return "The tree is empty"
        else:
            self.output = ''
            self.print_tree(self.root)
            return self.output

    def add(self, input):
        try:
            input_node = None

            # Check input type
            if type(input) == int:
                input_node = BSTNode(input)
            elif type(input) == BSTNode:
                input_node = input
            else:
                raise ValueError(
                    f"Arguement value '{input}' is not of type 'Binary Search Tree Node' or 'integer'.")

            if self.root is None:
                self.root = input_node
            elif input_node.data in self.contents:
                raise ValueError(
                    f"{input_node.data} Already exists within the tree.")
            else:
                def add_node(current_node, new_node):
                    if current_node.data < new_node.data:
                        if current_node.right:
                            add_node(current_node.right, new_node)
                        else:
                            current_node.right = new_node
                    else:
                        if current_node.left:
                            add_node(current_node.left, new_node)
                        else:
                            current_node.left = new_node

                add_node(self.root, input_node)
            self.contents.append(input_node.data)
        except ValueError as err:
            print(f"Value Error: {err}")

    def remove(self, input):
        try:
            input_data = None

            # Check input type
            if type(input) == int:
                input_data = input
            elif type(input) == BSTNode:
                input_data = input.data
            else:
                raise ValueError(
                    f"Arguement value '{input}' is not of type 'Binary Search Tree Node' or 'integer'.")

            if input_data not in self.contents:
                raise ValueError(
                    f"Arguement value '{input_data}' is not part if the tree.")
            else:
                def remove_node(current_node, remove_value, prev_node=None):
                    if current_node.data == remove_value:
                        if current_node.left and current_node.right:  # current_node has 2 children
                            if prev_node:
                                if prev_node.right is current_node:
                                    prev_node.right = None
                                else:
                                    prev_node.left = None
                            else:
                                self.root = None

                            self.contents.remove(remove_value)
                            self.nodes = [*self.contents]

                            for node in self.nodes:
                                self.contents.remove(node)
                            for node in self.nodes:
                                self.add(node)
                        elif current_node.right or current_node.left:  # current_node has 1 child
                            if current_node.right:
                                if prev_node.right is current_node:
                                    prev_node.right = current_node.right
                                else:
                                    prev_node.right = current_node.right
                            else:
                                if prev_node.left is current_node:
                                    prev_node.left = current_node.left
                                else:
                                    prev_node.left = current_node.left
                            self.contents.remove(remove_value)
                        else:  # current_node has 0 children
                            if prev_node.right is current_node:
                                prev_node.right == None
                            else:
                                prev_node.left = None
                            self.contents.remove(remove_value)
                    else:
                        if remove_value > current_node.data:
                            remove_node(current_node.right,
                                        remove_value, current_node)
                        else:
                            remove_node(current_node.left,
                                        remove_value, current_node)
                remove_node(self.root, input_data)
        except ValueError as err:
            print(f"Value Error: {err}")


bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

# create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)

print(bst)
print("--------------------------------------------------------")

bst.remove(1)  # leaf/end node
print(bst)
print("--------------------------------------------------------")

bst.remove(10)  # middle node
print(bst)
print("--------------------------------------------------------")

bst.remove(8)
print(bst)
print("--------------------------------------------------------")
