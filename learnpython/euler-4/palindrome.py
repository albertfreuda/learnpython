import math

# Function that determines whether an integer is a palindrome number
def ispalindrome(some_int):
    # Convert int to str
    my_string = str(some_int)
    # Split string into individual characters
    my_list   = list(my_string)
    # Determine how many digits are in the number
    num = len(my_list)
    # Prepare to loop over number from both sides
    N = math.floor(num/2)
    # Check whether first and last characters match and so on...
    for i in range(N):
        if(my_list[i]==my_list[num-1-i]):
            continue
        else: # If they don't match return 0
            return 0
    # If everything matched return 1
    return 1

det_rigtige_tal = 1


for x in range(100,1000):
    for y in range(100,1000):
        mit_tal  = x*y
        kriterie = ispalindrome(mit_tal)
        if kriterie == 1:
            if mit_tal > det_rigtige_tal:
                det_rigtige_tal = mit_tal

print(det_rigtige_tal)

