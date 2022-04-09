fibNum  = 1
fibNum2 = 1

bigSum = 0
iterNum = 0

upper_limit = 4000000

while(fibNum<upper_limit) and (iterNum<1000):
    iterNum += 1
    if(fibNum%2 == 0):
        bigSum += fibNum
    fibNum2 += fibNum
    fibNum = fibNum2-fibNum

print("Sum of all even fibonacci numbers below %i is %i" % (upper_limit,bigSum))
