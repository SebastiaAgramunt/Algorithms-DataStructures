class Queue:
    def __init__(self):
        self.queue = []

    def add(self, val):
        self.queue.append(val)

    def pop(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            del self.queue[0]
            return val
        else:
            return None


if __name__ == "__main__":

    q = Queue()

    q.add(0)
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)

    print("The queue so far is {}".format(q.queue))

    print("Popping {}".format(q.pop()))
    print("Popping {}".format(q.pop()))
    print("Popping {}".format(q.pop()))

    print("The queue is now {}".format(q.queue))
