# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    elements = []

    def size(self):
        size = 0
        for x in self.elements:
            size += 1
        return size

    def push(self, elem):
        self.elements[self.size():] = [elem]

    def pop(self):
        last_elem = self.elements[self.size() - 1]
        del self.elements[self.size() - 1]
        return last_elem

tokmindegy = Stack()
tokmindegy.push("bab")
tokmindegy.push("bab")
tokmindegy.push("bab")
tokmindegy.push("bab")
tokmindegy.push("bab")

print tokmindegy.pop()
print tokmindegy.size()
