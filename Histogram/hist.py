import matplotlib.pyplot as plt  

population_ages=[22,55,62,45,21,22,34,42,38,6,99,102,110,120,121,122,130,111,114,111,80,65,54,44,34,43,49]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.6)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram Data')
plt.legend()

plt.show()