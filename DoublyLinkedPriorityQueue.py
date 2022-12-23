class Node:	
	def __init__(self):
		self.info = 0
		self.priority = 0
		self.next = None
		self.prev = None

front = None
rear = None

def push(fr, rr, n, p):	
	global front, rear
	news = Node()
	news.info = n
	news.priority = p
	if (fr == None):
		fr = news
		rr = news
		news.next = None
	
	else:
		if (p <= (fr).priority):
			news.next = fr
			(fr).prev = news.next
			fr = news
		elif (p > (rr).priority):
			news.next = None
			(rr).next = news
			news.prev = (rr).next
			rr = news
		else:
			start = (fr).next
			while (start.priority > p):
				start = start.next
				
			(start.prev).next = news
			news.next = start.prev
			news.prev = (start.prev).next
			start.prev = news.next
			
	front = fr
	rear = rr
	
def peek(fr):
	return fr.info
			
def isEmpty(fr):
	return fr == None

def pop(fr, rr):
	
	global front , rear
	temp = fr
	res = temp.info
	(fr) = (fr).next
	
	if (fr == None):
		rr = None
		
	front = fr
	rear = rr
	return res

# Driver code
if __name__=='__main__':
	
	push( front, rear, 2, 3)
	push( front, rear, 3, 4)
	push( front, rear, 4, 5)
	push( front, rear, 5, 6)
	push( front, rear, 6, 7)
	push( front, rear, 1, 2)
	
	print(pop(front, rear))
	print(peek(front))

