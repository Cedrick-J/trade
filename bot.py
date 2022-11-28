import datetime
from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()
    date = datetime.datetime.now();
    trans = gettrans();
    lastbid = 'Profit' if trans[0]['profit']>0 else 'Loss';

    log = open("log2.txt","a") 
    log.write('\n'+date.strftime("%Y-%m-%d %H:%M:%S")+':\n'+"  Prediction :"+prediction+
    "\n  lastPrediction => "+lastPrediction+"\n  "+lastbid+'\n')
    log.close();
    
    lastPrediction = prediction;
    checkDirection(prediction);
    sleep(2700);