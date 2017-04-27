class Node(object):

    def __init__(self, label):
        self.label = label
        self.first = None
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.list = []
