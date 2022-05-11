#Find the largest prime factor of the following number:
# https://projecteuler.net/problem=3
number = 600851475143 

# It is easier to find the smallest prime factor:

def smallest_prime_factor(n):
    # Make sure input is sensible
    assert n>=2
    # Now divide n by smallest numbers until we find a factor
    for i in range(2,n+1):
        # Lowest factor will always be prime
        if n % i == 0:
            # Return the lowest factor
            return i
        

# Now, we know how to find the smallest prime factor.
# But we seek the largest! We can however divide the smallest one out 
# until we reach a prime number!


while True:
    p = smallest_prime_factor(number)
    if p != number:
        number //= p
    else:
        print(number)
        break

