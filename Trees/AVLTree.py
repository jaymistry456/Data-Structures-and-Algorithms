class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        else:
            if key < node.key:
                self._insert_recursive(node.left, key)
            elif key > node.key:
                self._insert_recursive(node.right, key)
            # Key already exists in the tree
            else:
                return
        self.root.height = 1 + max(self._get_height(self.root.left), self._get_height(self.root.right))
        self._balance(key)

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
                elif node.right is None:
                    node = node.left
            # If node has two children
            else:
                min_node = self._min_recursive(node.right)
                node.key = min_node.key
                self._delete_recursive(node.right, min_node.key)
        self.root.height = 1 + max(self._get_height(self.root.left), self._get_height(self.root.right))
        self._balance(key)

    def _balance(self, key):
        balance = self._get_balance(self.root)

        # LL Case
        if balance > 1 and key < self.root.left.key:
            self._right_rotate(self.root)
        # LR Case
        if balance > 1 and key > self.root.right.key:
            self.root.left = self._left_rotate(self.root.left)
            self._right_rotate(self.root)
        # RR Case
        if balance < -1 and key > self.root.right.key:
            self._right_rotate(self.root)
        # RL Case
        if balance < -1 and key < self.root.right.key:
            self.root.right = self._right_rotate(self.root.right)
            self._left_rotate(self.root)

    def _right_rotate(self, z):
        # T1 and T2 are x's left and right subtrees respectively
        # T3 is y's right subtree
        # T4 is z's left subtree
        #          z
        #        /   \
        #       y     T4
        #      /  \
        #     x    T3
        #   /   \
        #  T1   T2
        y = z.left
        T3 = y.right

        # Performing right rotation on z
        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _left_rotate(self, z):
        # T1 is z's left subtree
        # T2 is y's left subtree
        # T3 and T4 are x's left and right subtrees respectively
        #     z
        #   /   \
        #  T1    y
        #       /  \
        #     T2    x
        #          /  \
        #         T3   T4
        y = z.right
        T2 = y.left

        # Performing left rotation on z
        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def height_of_tree(self):
        # Height of AVL tree is not zero-based (height of the leaf nodes is 1 as set by the Node class)
        self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        else:
            return self._get_height(node.left) - self._get_height(node.right)

    def min(self):
        if self.root is None:
            return
        else:
            self._min_recursive(self.root)

    def _min_recursive(self, node):
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        if self.root is None:
            return
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

    def count_number_of_nodes(self):
        if self.root is None:
            return 0
        else:
            return self._count_number_of_nodes_recursive(self.root)

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
