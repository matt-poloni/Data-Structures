import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur = self
        while (nxt := cur.left if value < cur.value else cur.right) is not None:
            cur = nxt
        node = BinarySearchTree(value)
        if value < cur.value:
            cur.left = node
        else:
            cur.right = node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur = self
        found = cur.value == target
        while not found:
            nxt = cur.left if target < cur.value else cur.right
            if nxt is None:
                break
            cur = nxt
            found = cur.value == target
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        cur = self
        while cur.right is not None:
            cur = cur.right
        return cur.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            if (left := q.storage.head.left) is not None:
                q.enqueue(left)
            if (right := q.storage.head.right) is not None:
                q.enqueue(right)
            print(q.dequeue())

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while s.size > 0:
            if (left := s.storage.head.left) is not None:
                s.push(left)
            if (right := s.storage.head.right) is not None:
                s.push(right)
            print(s.pop())

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
