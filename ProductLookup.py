# ProductLookup.py

import bottlenose
import string
import xlwt
import time


def ASINLookup(ASIN, x, y):  # x is looping through ASINs. y for time
    amazon = bottlenose.Amazon(
        'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
        'ryane-20')
    for attempts in range(1, 10):
        try:
            product = amazon.ItemLookup(
                ItemId=ASIN, ResponseGroup='SalesRank,ItemAttributes')
        except:
            print "HTML/Internet Connection Error"
            time.sleep(.5)

        else:
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
                SalesRank = 'No Sales Rank Found'
            else:
                SR = Response[SRPos - 30:SRPos]
                SalesRank = SR.translate(None, IsolateSalesRank)
                # strip all chars, except for digits, leaving only the SalesRank
                # behind
            print SalesRank

            try:
                Sheet.write(x + 1, 1 + y, int(SalesRank))
            except ValueError:
                Sheet.write(x + 1, 1 + y, SalesRank)
            break
    else: #Multiple Attempts have failed
        print "Damn."
        if y == 1:  # Only find category the first time        
            Sheet.write(x + 1, 0, ASIN)  # Only write ASIN the first time
            Sheet.write(x + 1, 1, "Internet Error")  # Only write category the first time
        Sheet.write(x + 1, 1 + y, "Internet Error")




OrigTime = time.strftime('%c %z', time.localtime())
FileStart = time.strftime('%m%d_%H%M', time.localtime())
ASINText = open('ASINTest.txt', 'r') 

D=ASINText.read()
print D
ASINs= D.split('\n')


wbk = xlwt.Workbook()
Sheet = wbk.add_sheet('Product Sales Rank Data', cell_overwrite_ok=True)

Sheet.write(0, 0, "ASIN")
Sheet.write(0, 1, "Category")

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'


for j in range(1, 4):  # 11 is number of hours to check. First j always 1
    startTime = time.strftime('%c %z', time.localtime())
    Sheet.write(0, j + 1, "Sales Rank" + startTime)
    eTs = time.clock()
    for i in range(1, len(ASINs) + 1):
        ASINLookup(ASINs[i - 1], i, j)
        print "Searching Product " + str(i) + " of " + str(len(ASINs))
        # time.sleep(.5)
    wbk.save('AmazonSalesRankData' + FileStart + '.xls') 
    eTf = time.clock()
    elapsedTime = eTf - eTs
    print 'Elapsed Time = ' + str(elapsedTime)
    if elapsedTime < 3600:
        print "Finished Hour " + str(j) + " at " + str(time.strftime('%X %z', time.localtime()))
        time.sleep(60-elapsedTime)
