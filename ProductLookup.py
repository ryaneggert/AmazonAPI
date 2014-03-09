# ProductLookup.py

import bottlenose  # Amazon P.A. API bindings
import string
import xlwt  # Write to MS Excel file
import time  # Schedule data collection


def ASINLookup(ASIN, x, y):  # x is looping through ASINs. y for time
    amazon = bottlenose.Amazon(
        'AKIAI4I6EMMUJQXSGCFA', '/QTXbjXBMJk75UsOxNbAhRwkk0aVjPAKUla+ofaM',
        'ryane-20')

    # Rapid requests periodically fail. Code reattempts failed requests a set 
    # number of times. This number has been tested, and it minimizes the number  
    # of valueless returns while not devoting too much time to repeat requests.
    for attempts in range(1, 10):
        try:
            # Attempt API call
            product = amazon.ItemLookup( 
                ItemId=ASIN, ResponseGroup='SalesRank,ItemAttributes') 
        except:
            print "HTML/Internet Connection Error" #Display error msg.
            time.sleep(.5) #Wait before retrying

        else:
            Response = str(product)

            SRPos = Response.find('</SalesRank>')

            if y == 1:  # Only find category the first time
                CgPos = Response.find('</ProductGroup>')

                # If the program didn't find a category in the XML
                if CgPos == -1:
                    Category = 'No Category Found'
                else:
                    Cg = Response[CgPos - 40:CgPos]
                    Cat = Cg.split(">")
                    Category = Cat[-1]
                print Category
                Sheet.write(x + 1, 0, ASIN)  # Only write ASIN the first time
                # Only write category the first time
                Sheet.write(x + 1, 1, Category)

            # If the program didn't find a sales rank in the XML
            if SRPos == -1:
                SalesRank = 'Unranked'
            else:
                SR = Response[SRPos - 30:SRPos]
                SalesRank = SR.translate(None, IsolateSalesRank)
                # strip all chars, except for digits, leaving only the
                # SalesRank behind
            print SalesRank

            try:
                Sheet.write(x + 1, 1 + y, int(SalesRank))
            except ValueError:
                Sheet.write(x + 1, 1 + y, SalesRank)
            break #Leave loop on successful product loopkup process
    else:  # Multiple Attempts have failed
        print "Fiddlesticks."  # Oh bother.
        if y == 1:  # Only find category the first time
            Sheet.write(x + 1, 0, ASIN)  # Only write ASIN the first time
            # Only write category the first time
            Sheet.write(x + 1, 1, "Internet Error")
        Sheet.write(x + 1, 1 + y, "Internet Error")


OrigTime = time.strftime('%c %z', time.localtime())
FileStart = time.strftime('%m%d_%H%M', time.localtime())
ASINText = open('ASINsFin.txt', 'r')

RwIn = ASINText.read()  # Raw Input

ASINs = RwIn.split('\n') # Split into list of ASINs


wbk = xlwt.Workbook()  # Create workbook object
Sheet = wbk.add_sheet('Product Sales Rank Data', cell_overwrite_ok=True)

#Column Headers
Sheet.write(0, 0, "ASIN") 
Sheet.write(0, 1, "Category")

IsolateSalesRank = string.ascii_letters + '<>/'
IsolateCategory = '<>/'

RunT = 40 #Number of hours to check.
for j in range(1, RunT+1):  # RunT+1 to make range() inclusive. First j always 1
    startTime = time.strftime('%c %z', time.localtime())
    Sheet.write(0, j + 1, "Sales Rank" + startTime)
    eTs = time.clock()
    for i in range(1, len(ASINs) + 1):
        ASINLookup(ASINs[i - 1], i, j)
        print "Searching Product " + str(i) + " of " + str(len(ASINs))
        # time.sleep(.5) # Not needed. Pause only on fail condition

    #Dynamically name file to prevent overwrite
    wbk.save('AmazonSalesRankData' + FileStart + '.xls') 
    eTf = time.clock()
    elapsedTime = eTf - eTs  # Elapsed time of each loop iteration
    print 'Elapsed Time = ' + str(elapsedTime)
    if elapsedTime < 3600:
        print("Finished Hour " + str(j) + " at " +
              str(time.strftime('%X %z', time.localtime())))
        time.sleep(3600 - elapsedTime)
