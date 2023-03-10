class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.child = None

def newNode(data):
	return Node(data)

def MultiLinkedList(head):
	if not head:
		return
	temp = head
	while(temp.next != None):
		temp = temp.next
	currNode = head
	while(currNode != temp):
		if(currNode.child):
			temp.next = currNode.child
			tmp = currNode.child
			while(tmp.next):
				tmp = tmp.next
			temp = tmp
		currNode = currNode.next

def printList(head):
	if not head:
		return
	while(head):
		print("{}".format(head.data), end = " ---> ")
		head = head.next

# Driver code
if __name__=='__main__':
	
	# Child list of 13
	child13 = newNode(16)
	child13.child = newNode(3)
	
	# Child List of 10
	head1 = newNode(4)
	head1.next = newNode(20)
	head1.next.child = newNode(2) #Child of 20
	head1.next.next = newNode(13)
	head1.next.next.child = child13
	
	# Child of 9
	child9 = newNode(19)
	child9.next = newNode(15)

	# Child List of 17
	child17 = newNode(9)
	child17.next = newNode(8)
	child17.child = child9

	# Child List of 7
	head2 = newNode(17)
	head2.next = newNode(6)
	head2.child = child17
	
	# Main List
	head = newNode(10)
	head.child = head1
	head.next = newNode(5)
	head.next.next = newNode(12)
	head.next.next.next = newNode(7)
	head.next.next.next.child = head2
	head.next.next.next.next = newNode(11)

	MultiLinkedList(head)

	print("Multi Linked List is: ", end = "")
	printList(head)
