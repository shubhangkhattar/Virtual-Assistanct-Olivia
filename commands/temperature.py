import oliviaTTS as ot
import re
import urllib.request

def temperature(data):
    try:
                    data = data.split(' ')
                    
                    try:                    
                         if data[6]:
                              city = data[5]+data[6]

                    except:
                         city = data[5]
                         
                    print(city)                    
                    url = "http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
                    page = urllib.request.urlopen(url).read()
                    data1 = page.decode("utf-8")
                    m = re.search('span class="phrase">',data1)
                    start = m.end()
                    end = start +200
                    newString = data1[start:end]
                    
                    m = re.search('&deg',newString)
                    end=m.start()
                    start=end-4
                    maxt = newString[start:end]
                    if " " in maxt:
                        temp= maxt.split(" ")
                        maxt=temp[1]
                    print("max temp : " + maxt)
                    
                    newString=newString.split('&deg',1)
                    newdat=newString[1]
                    m = re.search('&deg',newdat)
                    end=m.start()
                    start=end-4
                    mint = newdat[start:end]
                    if " " in mint:
                        temp= mint.split(" ")
                        mint=temp[1]
                    print("min temp :  " + mint)

                    try:
                         ot.speak("The maximum Temperatue in "+str(data[5])+" "+str(data[6])+" is "+maxt+" degree celcius and minimum is " + mint + " degree celcius.")
                    except:
                         ot.speak("The maximum Temperatue in "+str(data[5])+" is "+maxt+" degree celcius and minimum is " + mint + " degree celcius.")
                    data=""
                    
    except:
                    ot.speak("there is no such city, try another")
