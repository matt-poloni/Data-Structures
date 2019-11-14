class Heap:
    def __init__(self):
        self.storage = []

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

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index > 0:
            p_index = (index - 1) // 2
            if self.storage[p_index] < self.storage[index]:
                self.storage[p_index], self.storage[index] = self.storage[index], self.storage[p_index]
                self._bubble_up(p_index)

    def _sift_down(self, index):
        if index < self.get_size() - 1:
            size = self.get_size()
            while (left := (index * 2) + 1) < size:
                child = left
                right = (index * 2) + 2
                if right < size and self.storage[left] < self.storage[right]:
                    child = right
                if self.storage[child] > self.storage[index]:
                    self.storage[child], self.storage[index] = self.storage[index], self.storage[child]
                    self._sift_down(child)
                else:
                    break
