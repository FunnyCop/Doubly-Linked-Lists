# Creating a node class
class xNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class xList:
    def __init__(self):
        self.head = None
        self.tail = None

    def xPrepend(self, value):
        node = xNode(value)
        node.next = self.head

        if self.head != None:
            self.head.prev = node
            self.head = node
            node.prev = None

        else:
            self.head = node
            self.tail = node
            node.prev = None

    def xAppend(self, value):
        node = xNode(value)
        node.prev = self.tail

        if self.tail == None:
            self.head = node
            self.tail = node
            node.next = None

        else:
            self.tail.next = node
            node.next = None
            self.tail = node

    def xPush_after(self, index_node, value):

        if index_node == None:
            print('Node is empty')

        if index_node != None:
            node = xNode(value)
            node.next = index_node.next
            index_node.next = node
            node.prev = index_node

            if node.next != None:
                node.next.prev = node

            if index_node == self.tail:
                self.tail = node

    def xPush_before(self, index_node, value):

        if index_node == None:
            print("Given node is empty")

        if index_node != None:
            node = xNode(value)
            node.prev = index_node.prev
            index_node.prev = node
            node.next = index_node

            if node.prev != None:
                node.prev.next = node

            if index_node == self.head:
                self.head = node
