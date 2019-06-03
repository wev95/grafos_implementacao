class Pilha():
    def __init__(self):
        self._array = []

    def push(self, item):
        self._array.append(item)

    def pop(self):
        return self._array.pop()
    
    def lenght(self):
        return len(self._array)