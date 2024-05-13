class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedLists:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, node):
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insert_at_begin(data)
        else:
            while current_node is not None and (position + 1) != index:
                current_node = current_node.next
                position = position + 1
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index Out of Range")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def update_node_at_index(self, data, index):
        if self.head is None:
            return
        else:
            current_node = self.head
            position = 0
            while current_node is not None and position != index:
                current_node = current_node.next
                position = position + 1
            if current_node is not None:
                current_node.data = data
            else:
                print("Index Out of Range")

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_at_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first()
        else:
            while current_node is not None and (position + 1) != index:
                current_node = current_node.next
                position = position + 1
            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index Out of Range")

    def remove_last(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def remove_node(self, data):
        if self.head is None:
            return
        current_node = self.head
        if current_node.data == data:
            self.remove_first()
        else:
            while current_node.next is not None and current_node.next.data != data:
                current_node = current_node.next
            if current_node.next is not None:
                current_node.next = current_node.next.next
            else:
                print("Data Not Found")

    def size_of_singly_linked_list(self):
        if self.head is None:
            return 0
        size = 0
        current_node = self.head
        while current_node is not None:
            size = size + 1
            current_node = current_node.next
        return size

    def print_singly_linked_list(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next

    def reverse_using_sliding_pointers(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        p = self.head
        q = None
        r = None
        while p is not None:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q

    def reverse_using_recursion(self, q, p):
        if self.head is None:
            return
        if self.head.next is None:
            return
        if p is not None:
            self.reverse_using_recursion(p, p.next)
            p.next = q
        else:
            self.head = q

    def identify_loop(self):
        p = self.head
        q = self.head
        while p.next is not None and q.next is not None:
            p = p.next
            q = q.next
            if q.next is not None:
                q = q.next
            if p is None or q is None:
                return
        if p == q:
            return True
        else:
            return False


def merge_sorted_linked_lists(ll1, ll2):
    first = ll1.head
    second = ll2.head
    if first.data <= second.data:
        third = first
        current_node = first
        first = first.next
        current_node.next = None
    else:
        third = second
        current_node = second
        second = second.next
        current_node.next = None
    while first is not None and second is not None:
        if first.data <= second.data:
            current_node.next = first
            current_node = first
            first = first.next
            current_node.next = None
        else:
            current_node.next = second
            current_node = current_node.next
            second = second.next
            current_node.next = None
    while first is not None:
        current_node.next = first
        current_node = current_node.next
        first = first.next
    while second is not None:
        current_node.next = second
        current_node = current_node.next
        second = second.next
