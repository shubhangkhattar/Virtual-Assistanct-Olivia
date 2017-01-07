import oliviaTTS as ot
import re
import urllib.request
import re
import urllib.request

def dictionary(data):
    
    try:
            url = "http://dictionary.reference.com/browse/"

            data=data.split(" ")

            word = data[5]
            print(word)

            url = url + word

            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")

            m = re.search('meta name="description" content="', data1)
            start = m.end()
            end = start + 300

            newString = data1[start:end]

            m = re.search("See more.",newString)
            end = m.start()-1

            defination = newString[0:end]
            ot.speak(defination)
            
    except:
           ot.speak("I'm sorry, you're word is not in the dictionary")
