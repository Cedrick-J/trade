from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()

    print()
    lastPrediction = prediction
    log = open("log2.txt","a") 
    e = datetime.datetime.now()
    log.write('\n\n'+e.strftime("%Y-%m-%d %H:%M:%S")+':\n'+"\Prediction "+prediction)
    "\nlastPrediction => "+lastPrediction)
    log.close()
    checkDirection(prediction);
    sleep(30)