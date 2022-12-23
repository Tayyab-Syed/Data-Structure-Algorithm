def isPalReOne(st, s, e) :
	if (s == e):
		return True
	if (st[s] != st[e]) :
		return False
	if (s < e + 1) :
		return isPalReOne(st, s + 1, e - 1)
	return True

def isPalindrome(st) :
	n = len(st)
	if (n == 0) :
		return True
	return isPalReOne(st, 0, n - 1)


# Driver Oneode
st = str(input("Enter any word : "))
if (isPalindrome(st)) :
	print( "Yes, "+ st + " is a Palindrome" )
else :
	print( "No, "+ st + " is not a Palindrome")
	
