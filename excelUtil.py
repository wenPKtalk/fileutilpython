import xlwt;

#设置表格样式
def set_style (name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold= bold
    font.height=height
    font.colour_index = 4
    style.font=font
    return style


def write_excel():
    f = xlwt.Workbook()
    sheet = f.add_sheet('学生',cell_overwrite_ok=True)
    row0 = []
    col0 = []
    #写第一行
    for i in range(0,len(row0)):
        sheet.write(0,i,row0[i],set_style('Times New Rowman',220,True))
    for i in range(0,len(col0)):
        sheet.write(i+1,i,col0[i],set_style('Times New Rowman',220,True))
    sheet.write(1,3,'2006/12/12')
    sheet.write(1,3,'2006/12/12')
    sheet.write(1,3,'2006/12/12')
    sheet.write(1,3,'2006/12/12')
    sheet.write(1,3,'2006/12/12')
    f.save("test.xls")

if __name__ == '__main__':
    write_excel()
    
