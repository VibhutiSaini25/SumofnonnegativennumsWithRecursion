def sumWithRecursion(n):
    if n==0:
        return 0
    return n+sumWithRecursion(n-1)


a=int(input())
print("Sum= ",sumWithRecursion(a))
