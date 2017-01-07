import oliviaTTS as ot
import random

def coin(data):
    
    coin=["tails","heads"]
    ot.speak("its "+random.choice(coin))
