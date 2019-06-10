class Fila():
    def __init__(self):
        self._array = []

    def add(self, element):
        self._array.append(element)

    def remove(self):
        return self._array.pop(0)

    def length(self):
        return len(self._array)
