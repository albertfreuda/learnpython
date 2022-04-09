# This program lists all number below N that are a multiple of either 3 or 5

# Top number
N = 1000

for sumIndex in range(1,N+1):
    sumVar = 0
    for number in range(1,sumIndex+1):
        if(number%3==0):
            sumVar += number
            continue
        if(number%5==0):
            sumVar += number
            continue
    print('Index: {ind}   Sum: {var}'.format(ind = sumIndex,var=sumVar))
