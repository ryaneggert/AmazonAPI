import bottlenose
import string

StripDig = string.ascii_letters + '<>/'
amazon = bottlenose.Amazon(
    'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
    'ryane-20')
product = amazon.ItemLookup(
    ItemId='B0094KNESM', ResponseGroup='SalesRank,ItemAttributes')
Response = str(product)

SRpos = Response.find('</SalesRank>')

SR = Response[SRpos - 30:SRpos]
print SR
SalesRank = SR.translate(None, StripDig)
print SalesRank
