from time import sleep
from functions import *

lastPrediction = ""
while True:
    prediction = getPrediction()

    print("\Prediction "+prediction)
    print("lastPrediction => "+lastPrediction)
    

    lastPrediction = prediction
    checkDirection(prediction);
    sleep(30);