# An alternative version of the same code

def compute(N):
    x = sum( i for i in range(1, N + 1) )
    y = sum(i*i for i in range(1,N+1))
    return x*x - y


print(compute(100))
