import xlwt
import datetime

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')
# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1, 0, label='this is test')

worksheet1 = workbook.add_sheet('My Worksheet1')    # 创建一个worksheet
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = 'Times New Roman'   # 字体名称
font.bold = True    # 黑体
font.underline = True   # 下划线
font.italic = True  # 斜体字
style.font = font   # 设定样式
# 写入excel   参数对应 行, 列, 值
worksheet1.write(0, 0, label='this is test')    # 不带样式的写入
worksheet1.write(1, 0, 'Formatted value', style)    # 带样式的写入
# 输入日期到单元格
style1 = xlwt.XFStyle()
style1.num_format_str = 'M/D/YY'
# Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
worksheet1.write(2, 0, datetime.datetime.now(), style1)    # 带样式的写入
# 向单元格添加一个超链接
worksheet1.write(3, 0, xlwt.Formula('HYPERLINK("http://www.baidu.com";"百度")'))

# 向单元格添加一个公式
worksheet2 = workbook.add_sheet('My Worksheet2')
worksheet2.write(0, 0, 5)   # Outputs 5
worksheet2.write(0, 1, 2)   # Outputs 2
worksheet2.write(1, 0, xlwt.Formula('A1*B1'))   # Should output "10" (A1[5] * A2[2])
worksheet2.write(1, 1, xlwt.Formula('SUM(A1,B1)'))  # Should output "7" (A1[5] + A2[2])

# 合并列和行
worksheet3 = workbook.add_sheet('My Worksheet3')
worksheet3.write_merge(0, 0, 0, 3, 'First Merge')
style3 = xlwt.XFStyle()
font3 = xlwt.Font()
font3.bold = True
style3.font = font3
worksheet3.write_merge(1, 2, 0, 3, 'Second Merge', style3)
# 合并第几行到几行的第几列到第几列
worksheet3.write_merge(4, 8, 0, 3, 'Second Merge', style3)

# 设置单元格内容的对齐方式
worksheet4 = workbook.add_sheet('My Worksheet4')
# 新建alignment
alignment = xlwt.Alignment()
# 设置行居中
# May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER
# 设置列居中
# May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER
style4 = xlwt.XFStyle() # Create Style
style4.alignment = alignment # Add Alignment to Style
worksheet4.write(0, 0, 'Cell Contents', style)

# 为单元格添加边框
borders = xlwt.Borders()
# DASHED虚线  NO_LINE没有  THIN实线
# May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED

borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

style4.borders = borders

# 设置背景颜色
pattern = xlwt.Pattern()
# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
pattern.pattern_fore_colour = 6
style4.pattern = pattern

worksheet4.write_merge(4, 8, 0, 3, 'Second Merge', style4)



# 保存
workbook.save('demo.xlsx')

