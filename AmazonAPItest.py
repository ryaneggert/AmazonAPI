import bottlenose
import string

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'
amazon = bottlenose.Amazon(
    'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
    'ryane-20')
product = amazon.ItemLookup(
    ItemId='B003S9VNWE', ResponseGroup='Large')
Response = str(product)
SRPos = Response.find('</SalesRank>')
CgPos = Response.find('</ProductGroup>')

if SRPos == -1:
    SalesRank = 'No Rank Found'
else:
    SR = Response[SRPos - 30:SRPos]
    SalesRank = SR.translate(None, IsolateSalesRank)
print SalesRank



Cg = Response[CgPos - 40:CgPos]
Cat = Cg.split(">")
Category = Cat[-1]
print Category
