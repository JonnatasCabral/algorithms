class Queue(object):

    def __init__(self):
        self.queue = []
        self.queue_len = 0

    def push(self, n):
            self.queue_len += 1
            self.queue.insert(0, n)

    def pop(self):
        if not self.is_empty():
            self.queue_len -= 1
            self.queue.pop(self.queue_len)

    def is_empty(self):
        if self.queue_len == 0:
            return True
        return False

queue = Queue()
queue.push(2)   # [2]
queue.push(54)  # [54, 2]
queue.push(1)   # [1, 54, 2]
queue.pop()     # [1, 54]
queue.pop()     # [1]

print queue.queue
