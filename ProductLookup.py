# ProductLookup.py

import bottlenose
import string
import xlwt


def ASINLookup(ASIN):
    for x in range(0, len(ASIN)):
        amazon = bottlenose.Amazon(
            'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
            'ryane-20')

        product = amazon.ItemLookup(
            ItemId=ASIN[x], ResponseGroup='SalesRank,ItemAttributes')
        Response = str(product)

        SRPos = Response.find('</SalesRank>')
        CgPos = Response.find('</ProductGroup>')

        if SRPos == -1:
            SalesRank = 'No Rank Found'
        else:
            SR = Response[SRPos - 30:SRPos]
            SalesRank = SR.translate(None, IsolateSalesRank)
        print SalesRank

        if CgPos == -1:
            Category = 'No Rank Found'
        else:
            Cg = Response[CgPos - 40:CgPos]
            Cat = Cg.split(">")
            Category = Cat[-1]
        print Category



IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'

ASINs = ['B003R248Q0', 'B002S53CN2', 'B005XLN97M', 'B003BLQEFA',
         'B004OFBJX4', 'B003S9VNWE', 'B007RDGJHG', 'B0002KZ4VI', 'B0038M5ILI']

ASINLookup(ASINs)












# for x in range(0, len(ASINs)):
#     amazon = bottlenose.Amazon(
#         'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
#         'ryane-20')

#     product = amazon.ItemLookup(
#         ItemId=ASINs[x], ResponseGroup='SalesRank,ItemAttributes')
#     Response = str(product)

#     SRPos = Response.find('</SalesRank>')
#     CgPos = Response.find('</ProductGroup>')

#     if SRPos == -1:
#         SalesRank = 'No Rank Found'
#     else:
#         SR = Response[SRPos - 30:SRPos]
#         SalesRank = SR.translate(None, IsolateSalesRank)
#     print SalesRank

#     if CgPos == -1:
#         Category = 'No Rank Found'
#     else:
#         Cg = Response[CgPos - 40:CgPos]
#         Cat = Cg.split(">")
#         Category = Cat[-1]
#     print Category



