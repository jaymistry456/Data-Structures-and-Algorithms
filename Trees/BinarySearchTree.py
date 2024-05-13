class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            node = Node(key)
        else:
            if key < node.key:
                self._insert_recursive(node.left, key)
            elif key > node.key:
                self._insert_recursive(node.right, key)
            # Key already exists in the tree
            else:
                return

    def delete(self, key):
        if self.root is None:
            return
        else:
            self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        # If key not found
        if node is None:
            return
        if key < node.key:
            self._delete_recursive(node.left, key)
        elif key > node.key:
            self._delete_recursive(node.right, key)
        # If node matches key
        else:
            # If node has no children
            if node.left is None and node.right is None:
                node = None
            # If node has one child
            elif node.left is None or node.right is None:
                if node.left is None:
                    node = node.right
                else:
                    node = node.left
            # If node has two children
            else:
                min_node = self._min_recursive(node.right)
                node.key = min_node.key
                self._delete_recursive(node.right, min_node.key)

    def min(self):
        if self.root is None:
            return None
        else:
            self._min_recursive(self.root)

    def _min_recursive(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        if self.root is None:
            return None
        else:
            self._max_recursive(self.root)

    def _max_recursive(self, node):
        while node.right is not None:
            node = node.right
        return node

    def depth_of_a_node(self, key):
        if self.root is None:
            return
        else:
            self._depth_of_a_node_recursive(self.root, key, 0)

    def _depth_of_a_node_recursive(self, node, key, current_depth):
        if node is None:
            return -1
        if key == node.key:
            return current_depth
        left_depth = self._depth_of_a_node_recursive(node.left, key, current_depth + 1)
        right_depth = self._depth_of_a_node_recursive(node.right, key, current_depth + 1)
        if left_depth != -1:
            return left_depth
        else:
            return right_depth

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
            self._count_number_of_nodes_recursive(self.root)

    def _count_number_of_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_number_of_nodes_recursive(node.left) + self._count_number_of_nodes_recursive(
                node.right)

    def in_order_traversal(self):
        if self.root is None:
            return
        else:
            self._in_order_traversal_recursive(self.root)

    def _in_order_traversal_recursive(self, node):
        if node is not None:
            self._in_order_traversal_recursive(node.left)
            print(node.key, end=' ')
            self._in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        if self.root is None:
            return
        else:
            self._pre_order_traversal_recursive(self.root)

    def _pre_order_traversal_recursive(self, node):
        if node is not None:
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)
            print(node.key, end=' ')

    def post_order_traversal(self):
        if self.root is None:
            return
        else:
            self._post_order_traversal_recursive(self.root)

    def _post_order_traversal_recursive(self, node):
        if node is not None:
            print(node.key, end=' ')
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
