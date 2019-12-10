import xlrd
from datetime import datetime,date

# 文件路径
file_path = '1.xlsx'
# 设置编码
xlrd.Book.encoding = 'utf8'
# 获取数据
data = xlrd.open_workbook(file_path)
# 获取所有的sheet
sheet = data.sheet_names()

for item in sheet:
	table = data.sheet_by_name(item)
	# print(item)
	# 取总行数
	# print(table.nrows)
	# 取总列数
	# print(table.ncols)
	print(item, "行数", table.nrows, "列数", table.ncols)

# sheet1的数据
sheet1_data = data.sheet_by_index(0)
sheet1_nrows = sheet1_data.nrows
sheet1_ncols = sheet1_data.ncols

for i in range(sheet1_nrows):
	for j in range(sheet1_ncols):
		# print(i, "※", j, end='  ')
		print(sheet1_data.cell(i,j).value, sheet1_data.cell(i,j).ctype, end=' ')
	print()











