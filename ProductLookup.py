# ProductLookup.py

import bottlenose
import string
import xlwt
import time

startTime = time.strftime('%c %z', time.localtime())

wbk = xlwt.Workbook()
Sheet = wbk.add_sheet('Product Sales Rank Data', cell_overwrite_ok=True)

Sheet.write(0, 0, "ASIN")
Sheet.write(0, 1, "Category")
Sheet.write(0, 2, "Sales Rank" + startTime)


def ASINLookup(ASIN, x, y):  # x is looping through ASINs. y for time
    amazon = bottlenose.Amazon(
        'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
        'ryane-20')

    product = amazon.ItemLookup(
        ItemId=ASIN, ResponseGroup='SalesRank,ItemAttributes')
    Response = str(product)

    SRPos = Response.find('</SalesRank>')

    if y == 1:
        CgPos = Response.find('</ProductGroup>')

        if CgPos == -1:
            Category = 'No Rank Found'
        else:
            Cg = Response[CgPos - 40:CgPos]
            Cat = Cg.split(">")
            Category = Cat[-1]
        print Category
        Sheet.write(x + 1, 0, ASIN)
        Sheet.write(x + 1, 1, Category)

    if SRPos == -1:
        SalesRank = 'No Rank Found'
    else:
        SR = Response[SRPos - 30:SRPos]
        SalesRank = SR.translate(None, IsolateSalesRank)
    print SalesRank
    Sheet.write(x + 1, 1 + y, SalesRank)

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'

ASINs = ['B003R248Q0', 'B002S53CN2', 'B005XLN97M', 'B003BLQEFA',
         'B004OFBJX4', 'B003S9VNWE', 'B007RDGJHG', 'B0002KZ4VI', 'B0038M5ILI']

j = 1  # Initially, only one iteration. No for loop to loop through hour delays
for j in range(1,10)
    for i in range(1, len(ASINs) + 1):
        ASINLookup(ASINs[i - 1], i, j)
        print "Searching Product " + str(i) + " of " + str(len(ASINs) + 1)
