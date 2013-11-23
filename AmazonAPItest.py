import bottlenose
import string

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'
amazon = bottlenose.Amazon(
    'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
    'ryane-20')
product = amazon.ItemLookup(
    ItemId='B0094KNESM', ResponseGroup='SalesRank,ItemAttributes')
Response = str(product)

SRPos = Response.find('</SalesRank>')
CgPos = Response.find('</ProductGroup>')

SR = Response[SRPos - 30:SRPos]
print SR
SalesRank = SR.translate(None, IsolateSalesRank)
print SalesRank

Cg = Response[CgPos - 40:CgPos]
print Cg
Cat = Cg.split(">")
Category = Cat[-1]
print Category
