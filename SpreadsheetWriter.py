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

# for x in xrange(1,10):
#     print x
#     print x * 6

import time

StartT = time.clock()

Listy= ['http://www.adorama.com/catalog.tpl?op=article_020705', 'http://www.adorama.com/catalog.tpl?op=article_022805', 'http://www.adorama.com/catalog.tpl?op=article_032805', 'http://www.adorama.com/catalog.tpl?op=article_041904', 'http://www.adorama.com/catalog.tpl?op=article_051704', 'http://www.adorama.com/catalog.tpl?op=article_052305', 'http://www.adorama.com/catalog.tpl?op=article_062104', 'http://www.adorama.com/catalog.tpl?op=article_071105', 'http://www.adorama.com/catalog.tpl?op=article_071204', 'http://www.adorama.com/catalog.tpl?op=article_090505', 'http://www.adorama.com/catalog.tpl?op=article_092605', 'http://www.adorama.com/catalog.tpl?op=article_101005', 'http://www.adorama.com/catalog.tpl?op=article_101705', 'http://www.adorama.com/catalog.tpl?op=article_102504', 'http://www.adorama.com/catalog.tpl?op=article_103105', 'http://www.adorama.com/catalog.tpl?op=article_112505', 'http://www.adorama.com/catalog.tpl?op=article_112805', 'http://www.adorama.com/catalog.tpl?op=article_122704']

print len(Listy) 

EndT = time.clock()

Elapsed = EndT - StartT

print Elapsed