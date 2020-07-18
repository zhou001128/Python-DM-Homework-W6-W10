import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
df=pd.DataFrame(pd.read_excel('争议性分析.xlsx'))
X = df['争议指数']
Y = df['互动力']
result1 = np.corrcoef(X, Y)
print(result1)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig=sns.pairplot(df)
fig.savefig("争议性分析.png")
