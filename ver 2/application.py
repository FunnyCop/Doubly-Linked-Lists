class xNode: # create Node class
    def __init__(self, value):
        self.value = value # Node's value
        self.next = None # next Node in List
        self.last = None # previous Node in list

class xList: # create List class
    def __init__(self):
        self.head = None # first Node in List
        self.tail = None # last Node in List
        self.index = 0 # number of Nodes in List

    # prepend to List or Node
    def xPrepend(self, value, index=None):
        node = xNode(value) # create new Node

        # create first Node
        if self.head == None: # if List is empty
            self.head = node # first Node = new Node
            self.tail = node # last Node = new Node
            self.index += 1 # index++
            return self

        # prepend to List
        elif index == None: # if no index is passed to the method
            node.next = self.head # new Node.next = first Node in List
            self.head = node # first Node in List = new Node
            node.next.last = node # first Node.last = new Node
            self.index += 1 # index++
            return self

        # prepend to Node
        else: # if the List contains Node(s) and an index is passed to the method
            if index > self.index - 1: # if given index is larger than the index of the List's last node
                print(f"Index {index} does not exist") # print error
                return self

            else: # if given index is not larger than the index of the List's last node
                runner = self.head # runner = reference_to(self.head)

                for x in range(index): # from 0 to index - 1
                    runner = runner.next # runner = reference_to(runner.next)

                if runner.last != None: # if runner is not the first Node in List
                    runner.last.next = node # index Node.last.next = new Node
                    node.last = runner.last # new Node.last = index Node.last

                runner.last = node # index Node.last = new Node
                node.next = runner # new Node.next = index Node

                if node.last == None: # if new Node is first Node in List
                    self.head = node

                self.index += 1 # index++
                return self

    # append to List or Node
    def xAppend(self, value, index=None):
        node = xNode(value) # create new Node

        # create first Node
        if self.head == None: # if List is empty
            self.xPrepend(value) # prepend to list
            return self

        # append to List
        elif index == None: # if no index is passed to the method
            node.last = self.tail # new Node.last = List.tail
            self.tail.next = node # List.tail.next = new Node
            self.tail = node # List.tail = new Node
            self.index += 1 # index++
            return self

        # append to Node
        else: # if the List contains Node(s) and an index is passed to the method
            if index > self.index - 1: # if given index is larger than the index of the List's last node
                print(f"Index {index} does not exist") # print error
                return self

            else: # if given index is not larger than the index of the List's last node
                runner = self.head # runner = reference_to(self.head)

                for x in range(index): # from 0 to index - 1
                    runner = runner.next # runner = reference_to(runner.next)

                if runner.next != None: # if runner is not the last Node in List
                    runner.next.last = node # index Node.next.last = new Node
                    node.next = runner.next # new Node.next = index Node.next

                runner.next = node # index Node.next = new Node
                node.last = runner # new Node.last = index Node

                if node.next == None: # if new Node is last Node in List
                    self.tail = node

                self.index += 1 # index++
                return self

    def xRemove(self, index):
        if index > self.index - 1:  # if given index is larger than the index of the List's last node
            print(f"Index {index} does not exist") # print error
            return self

        elif self.index == 0: # if List is empty
            print(f"List is empty") # print error

        else: # if given index is not larger that the length of List and List is not empty
            runner = self.head # runner = reference_to(self.head)

            for x in range(index): # from 0 to index - 1
                runner = runner.next # runner = reference_to(runner.next)

            if runner.last != None: # if index Node is not the first Node
                runner.last.next = runner.next # index Node.last.next = index Node.next

            if runner.next != None: # if index Node is not the last Node
                runner.next.last = runner.last # index Node.next.last = index Node.last

            del runner # delete object instance
            return self

arr = xList()
arr.xAppend(1).xAppend(2).xAppend(3).xAppend(4).xAppend(10, 2).xRemove(1)
runner = arr.head
while runner.next != None:
    print(runner.value)
    runner = runner.next
print(runner.value)

print(arr.head.value, arr.tail.value)