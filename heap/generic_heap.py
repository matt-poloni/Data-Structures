class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        last = self.get_size() - 1
        self._bubble_up(last)

    def delete(self):
        top = self.storage.pop(0)
        if self.get_size() > 0:
            last = self.storage.pop()
            self.storage.insert(0, last)
            self._sift_down(0)
        return top

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            p_index = (index - 1) // 2
            if self.comparator(self.storage[index], self.storage[p_index]):
                self.storage[p_index], self.storage[index] = self.storage[index], self.storage[p_index]
                self._bubble_up(p_index)

    def _sift_down(self, index):
        size = self.get_size()
        left = (index * 2) + 1
        if (right := (index * 2) + 2) < size:
            child = left if self.comparator(self.storage[left], self.storage[right]) else right
            if self.comparator(self.storage[child], self.storage[index]):
                self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
                self._sift_down(child)
        elif left < size:
            if self.comparator(self.storage[left], self.storage[index]):
                self.storage[left], self.storage[index] = self.storage[index], self.storage[left]
                self._sift_down(left)
