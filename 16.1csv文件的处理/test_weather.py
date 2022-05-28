from datetime import datetime
from matplotlib import pyplot as plt
import csv
filename1 = r'D:\python\vs python work\16.1csv文件的处理\sitka_weather_2014.csv'
filename2 = r'D:\python\vs python work\16.1csv文件的处理\death_valley_2014.csv'
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)
    dates1,highs1,lows1 =[],[],[]
    for row1 in reader1:
        try:
            current_date1 = datetime.strptime(row1[0],"%Y-%m-%d")
            high1 = int(row1[1])
            low1 = int(row1[3])
        except:
            print(current_date1,'missing data!')
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)
    dates2,highs2,lows2 =[],[],[]
    for row2 in reader2:
        try:
            current_date2 = datetime.strptime(row2[0],"%Y-%m-%d")
            high2 = int(row2[1])
            low2 = int(row2[3])
        except:
            print(current_date2,'missing data!')
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates1,highs1,c='red',alpha=1)
plt.plot(dates1,lows1,c='blue',alpha=1)
plt.plot(dates2,highs2,c='black',alpha=1)
plt.plot(dates2,lows2,c='green',alpha=1)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()