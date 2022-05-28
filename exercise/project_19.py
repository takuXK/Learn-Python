#EXCEL的读写
import xlrd,xlwt
#读取EXCEL工作表
filename = 'D:\\python\\vs python work\\exercise\\SCORE.xlsx'
scorexlsx = xlrd.open_workbook(filename)
scoresheet1 = scorexlsx.sheet_by_index(0)  #按sheet编号读取工作表
scoresheet2 = scorexlsx.sheet_by_name('Sheet1')  #按sheet名读取工作表
print(scoresheet1.nrows)  #查看工作表行数
print(scoresheet1.ncols)  #查看工作表列数
#通过索引访问工作表中的元素
c00 = scoresheet1.cell(0,0)
print(c00)
print(c00.ctype)  #类型
print(c00.value)  #值
#ctype为XL_CELL_TEXT类，返回1；
#xlrd.XL_CELL_NUMBER，返回2；
print(c00.ctype == xlrd.XL_CELL_TEXT)
print(scoresheet1.cell(1,1).ctype == xlrd.XL_CELL_NUMBER)
#按行取，按列取
print(scoresheet1.row(0))
print(scoresheet1.col(0))  #以上取值返回 类型:值
print(scoresheet1.row_values(0))  #仅返回值
print(scoresheet1.col_values(1,1))  #可类似切片操作，第1列，编号1开始的行一直到最后

#工作表添加元素
#sheet.put_cell(rowx,colx,ctype,value,xf_index(对其格式))
scoresheet1.put_cell(0,scoresheet1.ncols,xlrd.XL_CELL_TEXT,'总分',None)
print(scoresheet1.row_values(0))
#写入EXCEL工作表
wxlsx = xlwt.Workbook()  #创建xlsx文件
wsheet = wxlsx.add_sheet('test')  #创建工作表并命名
wsheet.write(0,0,'abc')  #wsheet.write(x,y,内容)
wxlsx.save('D:\\python\\vs python work\\exercise\\test.xls')




scorexlsx = xlrd.open_workbook(filename)
scoresheet = scorexlsx.sheet_by_index(0)
col_index = scoresheet.ncols  #现在最后列的索引
scoresheet.put_cell(0,col_index,xlrd.XL_CELL_TEXT,'总分',None)
#计算总分并添加
for i in range(1,scoresheet.nrows):
    total_score = sum(scoresheet.row_values(i,1))
    scoresheet.put_cell(i,col_index,xlrd.XL_CELL_NUMBER,total_score,None)
#写入EXCEL工作表
wscorexlsx = xlwt.Workbook()
wscoresheet = wscorexlsx.add_sheet(scoresheet.name)
for i in range(scoresheet.nrows):  #一个个写入
    for j in range(scoresheet.ncols):
        wscoresheet.write(i,j,scoresheet.cell_value(i,j))
wscorexlsx.save('D:\\python\\vs python work\\exercise\\output.xls')
