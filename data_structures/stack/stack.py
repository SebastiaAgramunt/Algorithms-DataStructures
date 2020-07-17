# Stack implementation in python


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack[-1]
            del self.stack[-1]
            return val
        else:
            return None


if __name__ == "__main__":
    s = Stack()

    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)

    print("Stack is now {}".format(s.stack))

    print("popping {}".format(s.pop()))
    print("popping {}".format(s.pop()))

    print("Stack is now {}".format(s.stack))
