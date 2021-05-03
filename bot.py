from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()

    print("\n1 Min => "+pred1min)
    print("lastPrediction => "+lastPrediction)
    

    lastPrediction = prediction
    checkDirection(prediction);
    sleep(30);