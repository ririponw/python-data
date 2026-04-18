import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway

excel_name = "data_202110546_박가은.xlsx"

# Q1 code here
import pandas as pd
df1 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q1")

mu1 = 150000

print(stats.ttest_1samp(df1.transportation,mu1,alternative='greater'))

# Q2 code here
df2 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q2")

print(stats.levene(df2.com,df2.elec))
print(stats.ttest_ind(df2.com,df2.elec,equal_var='True',alternative='two-sided'))

# Q3 code here
df3 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q3")

a = [547, 553, 549, 550, 546]
b = [555, 554, 558, 561,570]
c = [544,540,541,541,549]

print(f_oneway(a,b,c),'\n')

df3 = pd.DataFrame({'product':a+b+c,'group':np.repeat(['a','b','c'], repeats=5)})

tukey3 = pairwise_tukeyhsd(endog=df3['product'],groups=df3['group'],alpha=0.05)

print(tukey3)

# Q4 code here
df4 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q4")

model = ols('km ~ C(area) + C(ez)', data=df4).fit()
print(anova_lm(model))

print()

from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df4['km'], groups=df4['area'], alpha=0.05)
print(tukey)

tukey=pairwise_tukeyhsd(endog=df4['km'], groups=df4['ez'],alpha=0.05)
print(tukey)

# Q5 code here
df5 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q5")

import seaborn as sns
sns.regplot(x=df5.temp, y=df5.rain)
plt.show()

from statsmodels.formula.api import ols
res = ols('df5.temp ~ df5.rain', data=df5).fit()
print(res.summary())

corr=stats.pearsonr(df5.temp, df5.rain)
print(corr)

# Q6 code here
df6 = pd.read_excel(excel_name, engine='openpyxl', sheet_name="Q6")
obs = pd.DataFrame({'일':[297,160,58], '월':[362,242,45], '화':[335,177,39], '수':[412,256,48], '목':[412,276,60], '금':[425,263,53], '토':[352,221,51]})
obs.index=['일반국도','지방도','고속국도']
from scipy.stats import chi2_contingency
result6 = chi2_contingency(obs, correction = False)
print(result6)

################### Put your final exam answer here #####################################
print("1번 정답")
print("가설")
print("H0:실제 교통비=150000원")
print("H1:150000원<실제교통비")
print("p값 :0.278")
print("기각여부 :H1가설 기각")
print("결론 :실제 교통비는 150000원이다", '\n')

print("2번 정답")
print("가설")
print("H0:두 과의 모의토익성적에 차이가 없다")
print("H1:두 과의 모의토익성적에 차이가 있다")
print("p값 :0.042")
print("기각여부 :H0가설 기각")
print("결론 :두 과의 모의토익성적에 차이가 있다", '\n')

print("3번 정답")
print("가설")
print("H0:세 기계의 생산량에 차이가 없다.")
print("H1:세 기계의 생산량 중 적어도 하나는 다르다")
print("p값 :0.008")
print("기각여부 :H0가설 기각")
print("결론 :세 기계의 생산량 중 적어도 하나는 다르다")

print("다중비교결과 :기계2가 나머지 기계1, 3과 다르다", '\n')

print("4번 정답")
print("가설")
print("엔진에 따른 가설")
print("H0:세 엔진의 효과가 모두 같다")
print("H1:세 엔진의 효과 중 적어도 하나는 다르다")
print("p값 :0.0002")
print("기각여부 :H0 기각")
print("결론 :세 엔진의 효과 중 적어도 하나는 다르다", '\n')

print("정유사에 따른 가설")
print("H0:세 무연휘발유의 효과가 모두 같다")
print("H1:세 무연휘발유의 효과 중 적어도 하나는 다르다")
print("p값 :0.83")
print("기각여부 :H1 기각")
print("결론 :세 무연휘발유의 효과가 모두 같다")

print("다중비교결과 :엔진1이 나머지 엔진2,3과 다르다", '\n')

print("5번 정답")
print("(1) -0.733")
print("(2) 0.538")
print("(3) 강수량=14.2363-0.0010x온도", '\n')

print("6번 정답")
print("가설")
print("H0:도로 종류와 교통사고 건수는 무관하다")
print("H1:도로 종류와 교통사고 건수는 관련이 있다")
print("p값 :0.1087")
print("기각여부 :H1기각")
print("결론 :도로 종류와 교통사고 건수는 무관하다")
