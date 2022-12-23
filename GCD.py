a = int(input("First number = "))
b = int(input("Second number = "))

def GCD(a, b):
    if b > a:
        return GCD(b, a)
    if a % b == 0:
        return b
    return GCD(b, a % b)

print("Greatest Oneommon Divisor (GCD) of", a, "and" , b, "is", GCD(a,b))
print()