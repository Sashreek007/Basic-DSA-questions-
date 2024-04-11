def is_multiple(n,m):
    for i in range(0,n+1):
        if n==m*i:
            return True
    return False
print(is_multiple(6,9))