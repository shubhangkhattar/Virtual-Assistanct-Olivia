import oliviaTTS as ot
import re
import urllib.request

def stock(data):
    try:
            url = "https://www.google.com/finance?q="
            data = data.split(" ")
            stock = data[6]
            print(stock)
            url = url+stock
            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")
            m = re.search('meta itemprop="price"',data1)
            start = m.start()
            end = start+50
            newString = data1[start:end]
            m=re.search('content="',newString)
            start = m.end()
            newString1 = newString[start:]
            m = re.search("/",newString1)
            start=0
            end=m.end()-3
            final= newString1[0:end]
            ot.speak("The value of "+stock +" stock is "+final+" dollars")
            data=""

    except:
            ot.speak("Cannot retrive the stock price of " + stock + " try with something else")
            data=""
