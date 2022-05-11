# The answer is 232792560

def divisible(number):
    N = 21
    for i in range(1,N):
        if(number % i) != 0:
            return 0
        else:
            continue
    return 1




for number in range(1,1000000000):
    criteria = divisible(number)
    if criteria == 1:
        print(number)
        break
