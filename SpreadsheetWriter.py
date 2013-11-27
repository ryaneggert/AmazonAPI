# # import xlwt
# # import time


# # def SSWrite(Names, Sheet):
# #     for i in range(1, len(Names)+1):
# #         Sheet.write(i, 0, Names[i-1])
# #         print Names[i-1]

# # wbk = xlwt.Workbook()
# # Datasheet = wbk.add_sheet('Data', cell_overwrite_ok=True)


# # # Title
# # Datasheet.write(0, 0, "ASIN")
# # Datasheet.write(0, 1, "Category")
# # Datasheet.write(0, 2, "Sales Rank" + startTime)

# # List = ['George', 'Hank', 'Bill', 'Larry', 'John', 'Tipperary', 'Harold']

# # print len(List)

# # print range(1, 10)

# # print List[5]

# import urllib2 as u
# Response= u.urlopen('http://www.tutorialspoint.com/python/string_zfill.htm')

# Q = Response.read()

# List = Q.split('<')

# print List

# # SSWrite(List, Datasheet)

# # wbk.save('TestExcel.xls')

# K=0
# for i in range(1,20):
#     K += 5
#     print K
#     print
#     print

import time
Bob= time.strftime('%m%d_%H%M', time.localtime())

print "Go"+Bob+'.xls'
