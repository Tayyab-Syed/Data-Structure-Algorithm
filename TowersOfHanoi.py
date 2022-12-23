def tower(n, sourcePole, destinationPole, auxiliaryPole):
	# Base case (termination condition)
	if(0 == n):
		return
	tower(n-1, sourcePole, auxiliaryPole, destinationPole)
	print("Move the disk",sourcePole,"from",sourcePole,"to",destinationPole)
	tower(n-1, auxiliaryPole, destinationPole,sourcePole)


# Driver code
tower(4, 'S', 'D', 'A')
