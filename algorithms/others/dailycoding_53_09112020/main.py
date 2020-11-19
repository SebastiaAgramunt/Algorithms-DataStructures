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
    def __len__(self):
        return len(self.stack)


class TwoStackToQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val: int):
        self.stack1.add(val)

    def dequeue(self):
        if len(self.stack2) > 0:
            val = self.stack2.pop()
            return val
        elif len(self.stack1) > 0:
            while len(self.stack1) > 0:
                val = self.stack1.pop()
                self.stack2.add(val)
            val = self.stack2.pop()
            return val
        else:
            return None

    def __str__(self):
        s = f"\nStack 1: {self.stack1.stack}\n"
        s += f"Stack 2: {self.stack2.stack}"

        return s


if __name__ == "__main__":
    queue = TwoStackToQueue()

    print(f"Adding 1, 2, 3, 4")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue)

    print("Dequeuing...")
    val = queue.dequeue()
    print(f"Dequeued {val}")
    print(queue)

    print(f"Adding 5, 6")
    queue.enqueue(5)
    queue.enqueue(6)

    print(queue)
    print("Dequeuing...")
    val = queue.dequeue()
    print(val)
    print(queue)