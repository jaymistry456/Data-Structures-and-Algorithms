class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        new_node = Node(key)
        if node.left is None:
            node.left = new_node
        elif node.right is None:
            node.right = new_node
        else:
            if self._length_from_farthest_leaf(node.left) <= self._length_from_farthest_leaf(node.right):
                self._insert_recursive(node.left, key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        # If the binary tree does not exist
        if self.root is None:
            return
        # If the root node contains the key
        elif self.root.key == key:
            # If the root node does not have any children
            if self.root.left is None and self.root.right is None:
                return
            # If the root node contains only one child
            elif self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None:
                self.root = self.root.right
            # If the root node contains two children
            else:
                # Finding the in-order successor (and its parent) of the root node
                successor_parent, successor = self._find_successor_and_parent(self.root)
                # If the successor is the left child of its parent
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                # If the successor is the right child of its parent
                else:
                    successor_parent.right = successor.right
                # Replacing root node's key with the in-order successor's key
                self.root.key = successor.key
        # If the node to delete is any other node in the tree
        # Finding the node to delete, its parent and whether that node is the left or right child of the parent
        parent, node, is_left = self._find_node_and_parent(self.root, key)
        # If the key did not match any node in the binary tree
        if node is None:
            return
        # If the key matched a node in the tree
        # If that node does not have any children
        elif node.left is None and node.right is None:
            parent.left = None
        # If that node has one child
        elif node.left is None or node.right is None:
            # If the node to delete is the left child of its parent
            if is_left:
                # If the node has a left child only, we set its parent's left (as the node is the left child of the
                # parent) to point to left child of the node
                if node.left is not None:
                    parent.left = node.left
                # If the node has a right child only, we set its parent's left (as the node is the left child of the
                # parent) to point to right child of the node
                else:
                    parent.left = node.right
            # If the node to delete is the right child of its parent
            else:
                # If the node has a left child only, we set its parent's right (as the node is the right child of the
                # parent) to point to left child of the node
                if node.left is not None:
                    parent.right = node.left
                # If the node has a right child only, we set its parent's right (as the node is the right child of
                # the parent) to point to right child of the node
                else:
                    parent.right = node.right
        # If the node has two children
        else:
            # Finding the in-order successor (and its parent) of the node
            successor_parent, successor = self._find_successor_and_parent(node)
            # If the in-order is the left child of its parent, we point the successor's parent's left to point to the
            # successor's right as we are trying to promote the right subtree of the successor upwards
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            # If the in-order is the right child of its parent, we point the successor's parent's right to point to
            # the successor's right
            else:
                successor_parent.right = successor.right
            # Replacing the node's key with the successor's key effectively deleting the node from the binary tree
            node.key = successor.key

    def _find_node_and_parent(self, node, key):
        # If the node does not exist
        if node is None:
            return None, None, False  # parent, child, is_left
        # If the node exists and its left child exists and the left child matches the value
        elif node.left is not None and node.left.key == key:
            node.left = None
            return node, node.left, True  # parent, child, is_left
        # If the node exists and its right child exists and the right child matches the value
        elif node.right is not None and node.right.key == key:
            node.right = None
            return node, node.right, False  # parent, child, is_left
        # As the node and its children did not match the key, we go further down by
        # calling the function again but with node.left as the node
        parent, node, is_left = self._find_node_and_parent(node.left, key)
        # If the parent was None (no matching key was found),we go further down by
        # calling the function again but with node.right as the node
        if parent is None:
            parent, child, is_left = self._find_node_and_parent(node.right, key)
        return parent, child, is_left

    def _find_successor_and_parent(self, node):
        parent = node
        successor = node.right
        # Finding the left most node (and its parent) in the right subtree of the node which is the in-order successor
        while successor.left is not None:
            parent = successor
            successor = successor.left
        return parent, successor

    # Length of node from its farthest leaf
    def _length_from_farthest_leaf(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._length_from_farthest_leaf(node.left), self._length_from_farthest_leaf(node.right))

    # Depth of a node from root node
    def depth_of_a_node(self, key):
        if self.root is None:
            return
        else:
            self._depth_of_a_node_recursive(self.root, key, 0)

    def _depth_of_a_node_recursive(self, node, key, current_depth):
        # Key not found in any node
        if node is None:
            return -1
        # Key found in the current Node
        if node.key == key:
            return current_depth
        left_depth = self._depth_of_a_node_recursive(node.left, key, current_depth + 1)
        right_depth = self._depth_of_a_node_recursive(node.right, key, current_depth + 1)
        if left_depth != -1:
            return left_depth
        else:
            return right_depth

    # Height of the binary tree refers to the length of the longest path from the root to a leaf node
    def height_of_tree(self):
        if self.root is None:
            return
        else:
            self._height_of_tree_recursive(self.root)

    def _height_of_tree_recursive(self, node):
        if node is None:
            return -1
        else:
            return max(self._height_of_tree_recursive(node.left), self._height_of_tree_recursive(node.right)) + 1

    def count_number_of_nodes(self):
        if self.root is None:
            return
        else:
            self._height_of_tree_recursive(self.root)

    def _count_number_of_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return self._count_number_of_nodes_recursive(node.left) + self._count_number_of_nodes_recursive(
                node.right) + 1

    def in_order_traversal(self):
        self._in_order_traversal_recursive(self.root)

    def _in_order_traversal_recursive(self, node):
        if node is not None:
            self._in_order_traversal_recursive(node.left)
            print(node.key, end=' ')
            self._in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        self._pre_order_traversal_recursive(self.root)

    def _pre_order_traversal_recursive(self, node):
        if node is not None:
            print(node.key, end=' ')
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def post_order_traversal(self):
        self._post_order_traversal_recursive(self.root)

    def _post_order_traversal_recursive(self, node):
        if node is not None:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.key, end=' ')
