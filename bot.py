from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()

    print("\Prediction "+prediction)
    print("lastPrediction => "+lastPrediction)
    lastPrediction = prediction
    log = open("log2.txt","a") 
    e = datetime.datetime.now()
    log.write(e.strftime("%Y-%m-%d %H:%M:%S"))
    log.close()
    checkDirection(prediction);
    sleep(30)