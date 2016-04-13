class Stack(object):

    def __init__(self):
        self.stack = []
        self.stack_len = 0

    def push(self, n):
        self.stack.append(n)
        self.stack_len += 1

    def pop(self):
        if self.is_empty():
            print 'Stack Empty'
        else:
            self.stack_len -= 1
            print 'pop({})'.format(self.stack.pop(self.stack_len))

    def is_empty(self):
        if self.stack_len == 0:
            return True
        return False

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()

print stack.stack
