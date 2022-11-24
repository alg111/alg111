def factorial(n):
    r12 = 1
    for i in range(1,n+1):
        r12 *= i
    return r12

if __name__ == '__main__':
    print('factorial(10)=', factorial(10))