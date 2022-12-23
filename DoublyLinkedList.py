class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertionEmpList(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The list is empty")

    def InsertionEnd(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeletionStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None

    def DeletionEnd(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def PrintList(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

    def Search(self, target):
        i = 1
        Value = False
        curr = self.head
        if(self.head == None):
            print("List is empty")
            return
        while(curr != None):
            if(curr.item == target):
                Value = True
                break
            curr = curr.next
            i = i + 1
        if(Value):
            print("The node is present in the list at position : ")
            print(i)
        else:
            print("The node isn't present in the list")

# Driver Code
DoublyLList = doublyLinkedList()

print("Insertion :")
DoublyLList.InsertionEmpList(10)
DoublyLList.InsertionEnd(20)
DoublyLList.InsertionEnd(30)
DoublyLList.InsertionEnd(40)
DoublyLList.InsertionEnd(50)
DoublyLList.InsertionEnd(60)
DoublyLList.PrintList()

print("Deletion :")
DoublyLList.DeletionStart()
DoublyLList.DeletionStart()
DoublyLList.PrintList()

print("Searching :")
DoublyLList.Search(40)