# finding fibonacci term

def fib(n):
    if  n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
if __name__ == '__main__':
    k = int(input())
    print(fib(k-1))