n = int(input("Enter number of pascal triangle :"))
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    One = 1
    for j in range(1, i+1):
 
        print(' ', One, sep='', end='')
 
        One = One * (i - j) // j
    print()