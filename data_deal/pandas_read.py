#通过pandas库读取各种形式的数据
import pandas as pd

#txt
txtname = r'D:\python\vs python work\data_deal\Colors.txt'
colortable = pd.io.parsers.read_table(txtname)
print(colortable)

#csv
csvname = r'D:\python\vs python work\data_deal\titanic.csv'
titanic = pd.io.parsers.read_csv(csvname)
X = titanic[['age']].values  #列表形式
print(X)

#xls,xlsx
xlsname = r'D:\python\vs python work\data_deal\Values.xlsx'
xls = pd.ExcelFile(xlsname)
trig_values = xls.parse('Sheet1',index_col=None,na_values=['NA'])
#以上两部可合并为一步：
#trig_values = pd.read_excel(xlsname,'Sheet1',index_col=None,na_values=['NA'])
print(trig_values)