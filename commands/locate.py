import oliviaTTS as ot
import os


def locate(data):
    try:        
        
            if "where is" in data:
                print("here")
                data = data.split(" ")
                location = data[2]
    #Check for errors:            
            if "locate" in data:
                print("here")
                data = data.split(" ")
                location = data[1]
                 
                ot.speak("Hold on shoobhaang, I will show you where " + location + " is.")
                os.system("open -a safari https://www.google.nl/maps/place/" + location + "/&amp;")
                data=""
    except:
             ot.speak("There is no such company. Try again")
