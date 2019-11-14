class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        p_index = (index - 1) // 2
        if self.storage[p_index] < self.storage[index]:
            self.storage[p_index], self.storage[index] = self.storage[index], self.storage[p_index]
            self._bubble_up(p_index)

    def _sift_down(self, index):
        l_index = (index * 2) + 1
        r_index = (index * 2) + 2
        if self.storage[l_index] > self.storage[index]:
            self.storage[l_index], self.storage[index] = self.storage[index], self.storage[l_index]
            self._sift_down(l_index)
        elif self.storage[r_index] > self.storage[index]:
            self.storage[r_index], self.storage[index] = self.storage[index], self.storage[r_index]
            self._sift_down(r_index)
