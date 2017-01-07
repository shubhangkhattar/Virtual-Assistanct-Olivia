import speech_recognition as sr

 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
  
    data = ""
    
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("could not understand audio !")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("ERROR cannot request results")
        
    return data
