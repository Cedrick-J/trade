import json
import requests
import subprocess
from bs4 import BeautifulSoup

bid = 5000

#Get the predictions
def getPrediction(period):
    url = "https://m.investing.com/instrument/services/getTechnicalData"

    headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':'https://m.investing.com/currencies/gbp-usd-technical'}
    fields = {
    'period': '60', 
    'pairID': '2',
    'viewType':'normal'}
    source = requests.post(url, data = fields, headers = headers).text
    soup   = BeautifulSoup(source, 'lxml')
    bid    = soup.find('p',attrs={"class": "coloredBox"}).get_text()
    return bid;
    
#Get transaction results
def gettrans():
    output = subprocess.check_output(["php", "script.php", '{"op":"gettrans"}']).decode()
    return json.loads(output)['closed']
    
#Check if last 3 transactions were a succes
def lasttrans(trans):
    return True if trans[0]['profit']>0 and trans[1]['profit']>0 and trans[2]['profit']>0 else False

#Check diretion to bid
def checkDirection(prediction):
    if prediction == 'Strong Buy':
        print("Buy")
        makeBid(1);
    elif prediction == 'Strong Sell':
        print("Sell")
        makeBid(2);
    
#Check if last transaction was a success and change the bid accordingly
def makeBid(typ):
    global bid;
    trans = gettrans();
    if trans[0]['profit']>0:
    #Transaction was a profit
        if(lasttrans(trans)):
            bid=bid+(bid/4); placeBid(typ, bid);
        else: placeBid(typ, bid);
    else:
    #Transaction was a loss
        bid=bid-(bid/2); placeBid(typ, bid);
        
#Intiate a request to buy or sell        
def placeBid(typ, bid):
    print("Bid => "+str(bid));
    output = subprocess.check_output(["php", "script.php", '{"op":"placeBid", "val":"https://app.irontrade.com/ajax/openOperation?type='+str(typ)+'&stock=GBPUSD&interval=900&amount='+str(bid)+'accountId=4739813"}']).decode()
    print(output)