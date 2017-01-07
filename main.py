import oliviaSTT
from index import index
import oliviaTTS as ot
import time


time.sleep(2)
ot.speak("Hi shoobhaang, what can I do for you?")
while 1:

    data = oliviaSTT.recordAudio()
    index(data)
