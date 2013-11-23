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

    if y == 1:  # Only find category the first time
        CgPos = Response.find('</ProductGroup>')

        if CgPos == -1:  # If the program didn't find a category in the XML
            Category = 'No Category Found'
        else:
            Cg = Response[CgPos - 40:CgPos]
            Cat = Cg.split(">")
            Category = Cat[-1]
        print Category
        Sheet.write(x + 1, 0, ASIN)  # Only write ASIN the first time
        Sheet.write(x + 1, 1, Category)  # Only write category the first time

    if SRPos == -1:  # If the program didn't find a sales rank in the XML
        SalesRank = 'No Rank Found'
    else:
        SR = Response[SRPos - 30:SRPos]
        SalesRank = SR.translate(None, IsolateSalesRank)
        # strip all chars, except for digits, leaving only the SalesRank
        # behind
    print SalesRank
    Sheet.write(x + 1, 1 + y, SalesRank)

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'

ASINs = ['B003R248Q0', 'B002S53CN2', 'B005XLN97M', 'B003BLQEFA',
         'B004OFBJX4', 'B003S9VNWE', 'B007RDGJHG', 'B0002KZ4VI', 'B0038M5ILI']

for j in range(1, 11):  # 11 is number of hours to check. First j always 1
    for i in range(1, len(ASINs) + 1):
        ASINLookup(ASINs[i - 1], i, j)
        print "Searching Product " + str(i) + " of " + str(len(ASINs) + 1)
    wbk.save('AmazonSalesRankData.xls')  # ADD DATE TO FILENAME
