class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next

    def insert(self, new, position = None):
        if position == 1 or position is None:
            self.atEnd(new)
        elif position == 0:
            self.atBegining(new)
        else:
            self.inBetween(position, new)
        
    def atBegining(self, new):
        new = Node(new)
        new.next = self.head
        self.head = new

    def atEnd(self, new):
        new = Node(new)
        if self.head is None:
            self.head = new
            return
        last = self.head
        
        while last.next:
            last = last.next
        
        last.next = new

    def inBetween(self, middle_node, new):
        if middle_node is None:
            print("Mentioned node is absent")
            return
        new = Node(new)
        new.next = middle_node.next
        middle_node.next = new

    def remove(self, item):
        headVal = self.head
        if headVal:
            if headVal.data == item:
                self.head = headVal.next
                headVal = None
                return
        while headVal:
            if headVal.data == item:
                break
            prev = headVal
            headVal = headVal.next
        if headVal == None:
            return
        prev.next = headVal.next
        headVal = None


l = LinkedList()
l.head = Node(1)
a = Node(2)
b = Node(3)
l.head.next = a
a.next = b

l.insert(4)
l.remove(6)

l.print()
