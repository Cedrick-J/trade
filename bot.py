from time import sleep
from functions import *

lastPrediction = ""
while True:
    pred1min = getPrediction('60')
    pred5min = getPrediction('300')
    pred15min = getPrediction('900')
    print("\n1 Min => "+pred1min)
    print("5 Min => "+pred5min)
    print("15 Min =>"+pred15min)
    print("Last => "+lastPrediction)
    
#    if pred1min==pred5min:
#    if pred1min != lastPrediction:
#        lastPrediction = pred1min
#        checkDirection(pred1min);
    if pred15min != lastPrediction:
        lastPrediction = pred15min
        checkDirection(pred15min);
    else: print("Waiting")
    sleep(30);