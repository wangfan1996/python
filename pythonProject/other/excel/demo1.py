import xlwt

# 设置字体
def set_style(name, bold, underline, italic, pattern_colour):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.underline = underline
    font.italic = italic
    style.font = font
    # 对齐方式
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment
    # 设置背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    # 0 = Black 1 = White 2 = Red 3 = Green 4 = Blue 5 = Yellow 6 = Magenta 7 = Cyan
    pattern.pattern_fore_colour = pattern_colour
    style.pattern = pattern
    return style

# 写excel
def write_excel():
    f = xlwt.Workbook() # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet cell_overwrite_ok=True 可以覆盖原来单元格中数据
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
    status = [u'预订', u'出票', u'退票', u'业务小计']
    # 第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', True, False, False, 6))
    # 第一列和最后一列
    i, j = 1, 0
    while i < 4 * len(column0) and j < len(column0):
        sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', True, False, False, 7))  # 第一列
        sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
        i += 4
        j += 1
    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', True, True, True, 1))
    # 生成第二列
    i = 0
    while i < len(status) * len(column0):
        for j in range(0, len(status)):
            sheet1.write(j + i + 1, 1, status[j])
        i += len(status)

    f.save('demo1.xlsx')  # 保存文件

write_excel()