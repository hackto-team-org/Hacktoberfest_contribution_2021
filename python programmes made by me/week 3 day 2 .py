#just estimate
from statistics import mean
estimate=[100,6654,4644,4,485,4,4964,6497,3668,87,2,67,62524,68,8,47,687,5,78,5,4,5,12,1,25,6,4,65,78,5,4,5,54,5,212,54,5]
estimate.sort()
#print(estimate.sort())
tv=int(0.1*len(estimate))
estimate=estimate[tv:]
estimate=estimate[:len(estimate)-tv]
print (mean(estimate))



from scipy import stats
estimate=[100,6654,4644,4,485,4,4964,6497,3668,87,2,67,62524,68,8,47,687,5,78,5,4,5,12,1,25,6,4,65,78,5,4,5,54,5,212,54,5]
estimate.sort()
p=stats.trim_mean(estimate,.1)
print(p)

    
#plotting a graph
from matplotlib import pyplot as plt
plt.plot([1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],'bo')
plt.ylabel("students")
plt.xlabel("expenditure")
plt.plot([1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],'r--')
plt.plot([1,2,3,4,5,6,7,8,9],[9,8,7,6,5,4,3,2,1],'rs')


#plotting the estimates
import statistics 
import matplotlib.pyplot as plt
estimate=[100,6654,4644,4,485,4,4964,6497,3668,87,2,67,62524,68,8,47,687,5,78,5,4,5,12,1,25,6,4,65,78,5,4,5,54,5,212,54,5]
y=[]

plt.plot(estimate)
estimate.sort()
tv=int(0.1*(len(estimate)))
estimate=estimate[tv:]
estimate=estimate[:len(estimate)-tv]
for i in estimate:
    y.append(5)
plt.plot(estimate,y,'r--')
plt.plot(statistics.mean(estimate),5,'ro')
plt.plot(statistics.median(estimate),5,'bo')
    