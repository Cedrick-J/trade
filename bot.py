import datetime
from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()
    lastPrediction = prediction
    date = datetime.datetime.now();

    log = open("log2.txt","a") 
    log.write('\n\n'+date.strftime("%Y-%m-%d %H:%M:%S")+':\n'+"\Prediction :"+prediction+
    "\nlastPrediction => "+lastPrediction)
    log.close();
    
    checkDirection(prediction);
    sleep(30)