from commands import calculate
from commands import coin
from commands import creator
from commands import dictionary
from commands import goodbye
from commands import hru
from commands import iaf
from commands import locate
from commands import stock
from commands import temperature
from commands import time
from commands import wru



def index (data):

    if "how are you Olivia" in data:
        hru.hru(data)
            
    if "I am fine" in data:
        iaf.iaf(data)

    if "who are you" in data:
        wru.wru(data)
        
    if "who created you" in data:
        creator.creator(data)

    if "what time is it" in data:
        time.time(data)

    if "tell me the stock price of" in data:
        stock.stock(data)

    if "calculate" in data:
        calculate.calculate(data)
        
    if ( "where is" or "locate" ) in data:
        locate.locate(data)
        
    if ("goodbye Olivia" or "goodbye" ) in data:
        goodbye.goodbye(data)
        
    if ( "flip a coin" or "flip coin") in data:
        coin.coin(data)

    if "what is the temperature in" in data:
        temperature.temperature(data)

    if "what is the meaning of" in data:
        dictionary.dictionary(data)
    
