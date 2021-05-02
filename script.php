<?php
$bid   = 2000;
$trans = "https://app.irontrade.com/api/operations";
$sma6  = "https://www.alphavantage.co/query?function=SMA&symbol=GBPUSD&interval=1min&time_period=6&series_type=close&fastdmatype=0&apikey=3BDE1MTMJ048ETQV";
$sma14 = "https://www.alphavantage.co/query?function=SMA&symbol=GBPUSD&interval=1min&time_period=14&series_type=close&fastdmatype=0&apikey=3BDE1MTMJ048ETQV";
$headers[] = 'Origin: https://irontrade.com';
$headers[] = 'accept: */*';

$headers[] = 'X-Requested-With: com.full.iron';
$headers[] = 'sec-fetch-site: same-site';
$headers[] = 'sec-fetch-mode: cors';
$headers[] = 'sec-fetch-dest: empty';
$headers[] = 'accept-language:en-US,en;q=0.9';
$referer = 'https://irontrade.com/'; 
$useragent = 'Mozilla/5.0 (Linux; Android 9; TECNO KC6 Build/PPR1.180610.011; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[os: AndroidWeb, application_id: com.full.iron, version: 106, provider: IronTrade]_wvbo_full'; 

#Get sma
function getSma($url) {
   $output=file_get_contents($url);
   echo($output);

}
#Iron trade Api
function get($url) {
global $headers, $useragent, $referer;
  $ch = curl_init($url);
//Set cokies
  curl_setopt ($ch, CURLOPT_COOKIEFILE, 'cookies.txt'); 
//Set headers
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
  curl_setopt($ch, CURLOPT_HEADER, 0); 
//Set useragent
  curl_setopt($ch, CURLOPT_USERAGENT, $useragent);
//Set referer
  curl_setopt($ch, CURLOPT_REFERER, $referer);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt($ch, CURLINFO_HEADER_OUT, 0);
  $output = curl_exec($ch);
  curl_close($ch);
  echo($output);
}

if($argc > 1) {
  $json_str = $argv[1];
  $ops = json_decode($json_str, true);
if ($ops['op']=='gettrans') {
    get($trans);
}else if($ops['op']=='placeBid') {
    get($ops['val']);
}else if($ops['op']=='getSma') {
    getSma($ops['val']);
}}
/*foreach ($ops as $op => $fun) {
  echo("$op => $fun \n");
}*/
?>