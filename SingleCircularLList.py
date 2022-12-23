# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Circularlinkedlist():
#     def __init__(self):
#         self.head = None
        
#     def append(self,data):
#         if self.head == None:
#             self.head = Node(data)
#             self.head.next = self.head 
#         else:
#             new_node = Node(data)
#             curr = self.head
#             while curr.next != self.head:
#                 curr = curr.next
#             curr.next = new_node
#             new_node.next = self.head
               
#     def prepend(self,data):
#         new_node = Node(data)
#         curr = self.head
#         new_node.next = self.head
#         if self.head == None:
#             new_node.next = new_node
#         else:
#             while curr.next != self.head:
#                 curr = curr.next
#             curr.next = new_node
#         self.head = new_node

#     def printlist(self):
#         curr = self.head
#         while curr:
#             print(curr.data)
#             curr = curr.next
#             if curr == self.head:
#                 break

# obj = Circularlinkedlist()
# obj.append("X")
# obj.append("Y")
# obj.append("Z")
# obj.prepend("C")
# obj.prepend("B")
# obj.prepend("A")
# obj.printlist()


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularlinkedlist():
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
        
    def append(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head 
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
               
    def prepend(self,data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        if self.head == None:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break

obj = DoublyCircularlinkedlist()
obj.append("X")
obj.append("Y")
obj.append("Z")
obj.prepend("C")
obj.prepend("B")
obj.prepend("A")
obj.printlist()