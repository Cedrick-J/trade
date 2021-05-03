import json
import requests
import subprocess
from bs4 import BeautifulSoup

bid = 5000

#Get the predictions
def getprediction();
   url =  "https://ssltools.forexprostools.com/technical_summary.php?pairs=&curr-name-color=%230059B0&fields=1h&force_lang=1";
    headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':'https://m.investing./currencies/gbp-usd-technical'}
    
    source = requests.get(url2, headers=headers).text
    soup   = BeautifulSoup(source, 'lxml')
    data   = soup.find('tr',attrs={"class": "ftqa11 ftqtr1"}).contents[3]
    biddir = biddir.font.b.get_text()
    return biddir;
    
#Get transaction results
def gettrans():
    output = subprocess.check_output(["php", "script.php", '{"op":"gettrans"}']).decode()
    return json.loads(output)['data']
    
#Check if last 3 transactions were a succes
def lasttrans(trans):
    return True if trans[0]['profit']>0 and trans[1]['profit']>0 and trans[2]['profit']>0 else False

#Check diretion to bid
def checkDirection(prediction):
    if prediction == 'Strong Buy':
        makeBid(1);
    elif prediction == 'Strong Sell':
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
    log = open("log.txt","a") 
    log.write("\nBid => "+str(bid));
    output = subprocess.check_output(["php", "script.php", '{"op":"placeBid", "val":"https://app.irontrade.com/ajax/openOperation?type='+str(typ)+'&stock=EURUSD&interval=900&amount='+str(bid)+'accountId=4739813"}']).decode()
    log.write('\n'+output+'\n') 
    log.close()