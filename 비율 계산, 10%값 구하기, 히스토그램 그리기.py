import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("근무연수.xlsx")

plt.hist(data, label='bins=6', bins=6)
plt.legend()
plt.show()

from scipy.stats import norm

mu=160
sigma=3
percent_point=0.9

y=norm.cdf(-5/3, mu, sigma) #z=(155-160)/3

print('신장이 155cm 이하인 여성의 비율:',y) #
print('상위 10% 신장:',norm.ppf(percent_point,mu,sigma)) #163.8446546966338

from scipy.stats import norm
import math

mu=9.3
sigma=3.2
zl=9.3-1.96*(3.2/math.sqrt(250))

y=norm.cdf(zl,mu,sigma) #ZL=9.3-1.96(3.2/math.sqrt(250)), ZU=9.3+1.96(3.2/math.sqrt(250))

print('95%신뢰구간:',2*y) #95%신뢰구간: 0.9013459292364642

