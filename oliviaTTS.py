# gtts (google Text To Speech)package required.
# Install mpg321 using Home Brew if Mac User.

from gtts import gTTS
import os

def speak(oliviaReply):
    
    try:
 
        print("Olivia Said : "+oliviaReply)
        reply = gTTS(text=oliviaReply, lang='en')
        # Save the audio reply generated using Google Text To Speech.
        reply.save("reply.mp3")
        # Play the audio reply using mpg321.
        os.system("mpg321 reply.mp3")
        
    except:
        # Interent not available.
        print("ERROR : Internet not available.")
