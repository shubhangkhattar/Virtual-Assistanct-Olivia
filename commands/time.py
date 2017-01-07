import oliviaTTS as ot
from time import ctime


def time(data):
    ot.speak("Right now as per my clock it is " + ctime())
