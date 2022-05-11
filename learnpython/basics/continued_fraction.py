import matplotlib as mpl
import matplotlib.pyplot as plt

a = [1]

for i in range(10):
    number = 1/(1+a[i])
    a.append(number)

fig,ax = plt.subplots()
ax.plot(a,'kx')

plt.show()


for i in range(len(a)):
    print("%i %s"%(i,a[i]))
