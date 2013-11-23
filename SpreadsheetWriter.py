import xlwt
import time


def SSWrite(Names, Sheet):
    for i in range(1, len(Names)+1):
        Sheet.write(i, 0, Names[i-1])
        print Names[i-1]

wbk = xlwt.Workbook()
Datasheet = wbk.add_sheet('Data', cell_overwrite_ok=True)


startTime = time.strftime('%c %z', time.localtime())
# Title
Datasheet.write(0, 0, "ASIN")
Datasheet.write(0, 1, "Category")
Datasheet.write(0, 2, "Sales Rank" + startTime)

List = ['George', 'Hank', 'Bill', 'Larry', 'John', 'Tipperary', 'Harold']

print len(List)

print range(1, 1+len(List))

print List[5]

SSWrite(List, Datasheet)

wbk.save('TestExcel.xls')
