# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

x = 0
y = 0


for i in range(101):
    x += i
    y += i*i

delta = x*x - y

print(delta)
