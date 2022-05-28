import datetime as dt
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab as plb
df = pd.DataFrame(columns=('Time','Sales'))
start_date = dt.datetime(2020,7,1)
end_date = dt.datetime(2020,7,10)
date_range = pd.date_range(start_date,end_date)
for single_date in date_range:
    row = dict(
        zip(
            ['Time','Sales'],
            [single_date,int(50 * np.random.rand(1))]
        )  #zip将两列表组合成元组列表
    )
    row_s = pd.Series(row)  #将字典变为符合DataFrame的形式
    row_s.name = single_date.strftime('%b %d')
    df = df.append(row_s)

date = df.index.to_list()
sales = df['Sales'].values
print(sales)
plt.plot(date,sales,linestyle='--',color='b')
plt.ylim(0,50)
plt.xlabel('Sales Date')
plt.ylabel('Sales Value')
plt.title('Ploting Time')
plt.show()