from Array import Array

class Queue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Can not be empty"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item
    
    def traverse(self):
        assert not self.isEmpty()," cannot traverse through empty list"
        node = self._qhead
        
        while node:
            
            print(node.item)
            node = node.next

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class BoundedPri:
    def __init__(self,numLevel):
        self._qSize = 0
        self._qLevels = Array(numLevel)
        for i in range(numLevel):
            self._qLevels[i] = Queue()
        
    def isEmpty(self):
        return self._qSize == 0
    
    def __len__(self):
        return self._qSize
    
    def enqueue(self, item, priority):
        assert priority >= 0 and priority < len(self._qLevels), "Invalid priority"

        q = self._qLevels[priority]
        q.enqueue(item)
        self._qSize += 1
    
    def dequeue(self):
        assert not self.isEmpty(), "Empty queue"
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            if not q.isEmpty():
                self._qSize -= 1
                return q.dequeue()

    def peek(self):
        assert not self.isEmpty(), "Empty queue"
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            if not q.isEmpty():
                return q.peek()
    def traverse(self):
        for i in range(len(self._qLevels)):
            q = self._qLevels[i]
            q.traverse()

obj = BoundedPri(3)
obj.enqueue("A", 1)
obj.enqueue("B", 0)
obj.enqueue("C", 2)
obj.enqueue("D", 0)
obj.traverse()
print("Dequeue: ", obj.dequeue())
