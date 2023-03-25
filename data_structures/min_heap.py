import math

class MinHeap:
    def __init__(self):
        self.nodes = []
        self.length = 0

    def is_empty(self) -> bool:
        return self.length == 0

    def push(self, val: int) -> None:
        self.nodes.append(val)
        self.length += 1
        self._bubble_up()

    def peek(self) -> int:
        if self.length == 0:
            return None
        
        return self.nodes[0]

    def pop(self) -> int:
        if self.length == 0:
            return None
        
        if self.length == 1:
            self.length -= 1
            return self.nodes.pop()
        
        val = self.nodes[0]
        self.nodes[0] = self.nodes.pop()
        self.length -= 1
        self._bubble_down()

        return val

    def _parent(self, node: int) -> int or None:
        parent = math.ceil((node - 2) / 2)
        if parent >= 0:
            return parent

        return None

    def _left(self, node: int) -> int or None:
        left = node * 2 + 1
        if left <= self.length - 1:
            return left

        return None

    def _right(self, node: int) -> int or None:
        right = node * 2 + 2
        if right <= self.length - 1:
            return right

        return None

    def _bubble_up(self):
        node = self.length - 1
        parent = self._parent(node)

        while node > 0 and self._val(node) < self._val(parent):
            self._swap(node, parent)

            node = parent
            parent = self._parent(node)

    def _bubble_down(self):
        node = 0

        while self._has_children(node):
            smallest_child = self._smallest_child(node)
            if self._val(smallest_child) < self._val(node):
                self._swap(smallest_child, node)
                node = smallest_child
            else:
                break
            

    def _smallest_child(self, node: int) -> int:
        left = self._left(node)
        right = self._right(node)

        if right is None or self._val(left) < self._val(right):
            return left

        return right

    def _has_children(self, node: int) -> bool:
        left = self._left(node)
        if left is None:
            return False

        return True

    def _val(self, node: int) -> int:
        return self.nodes[node]

    def _swap(self, node1: int, node2: int):
        self.nodes[node1], self.nodes[node2] = self.nodes[node2], self.nodes[node1]
    

    #                        0
    #                  1           2
    #               3    4      5      6
    #              7 8  9 10  11 12  13 14