import requests
import json
import sys
import pprint


def main():
	m = getMarkets()
	items = m.items()
	values = m.values()
	for (n,v) in items:
		v1 = v[0]
		v2 = v[1]
		if(len(v1)>0):
			highBuy = max(v1)[0]
			print("highBuy:{0:.10f}".format(highBuy))
		else:
			print("v1{}".format(v1))
		if(len(v2)>0):
			lowSell = min(v2)[0]
			print("lowSell:{0:.10f}".format(lowSell))
		else:
			print("v2{}".format(v2))
		if(highBuy > lowSell):
			print ("yay:{}".format(n))
		#print(n)
		#v1 = v[0]
		#v2 = v[1]
		#print(v1)
		#print(min(v1))
		#print(max(v1)[0])
		#print(v2)
		#print(min(v2))
		#print(max(v2))
	#for v in values:
	#	v1 = v[0]
	#	v2 = v[1]
	#	print(v1)
	#	print(min(v1))
	#	print(max(v1))
		
			
def parseRates(inRate):
	return (inRate["Rate"],inRate["Quantity"])
	
def getMarkets():
		
	url = "https://bittrex.com/api/v1.1/public/getmarkets"
	marketsummaries = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
	orderBook = "https://bittrex.com/api/v1.1/public/getorderbook?market={0}&type=both" 
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(marketsummaries)
	data = response.json()
	numMarkets = len(data["result"])
	markets = dict()
	#print(json.dumps(data,indent=4))
	#print(numMarkets)
	for i in range(0,15):
		name = data["result"][i]["MarketName"]
		tempUrl = orderBook.format(name)
		resp = requests.get(tempUrl)
		d = resp.json()
		
		brez = d["result"]["buy"]
		srez = d["result"]["sell"]
		
		if(brez is not None):
			buyrates = list(map(lambda x: parseRates (x) ,d["result"]["buy"]))
		if(srez is not None):
			sellrates = list(map(lambda x: parseRates (x) ,d["result"]["sell"]))
		
		rateTup = (buyrates,sellrates)
		markets.update({name:rateTup})
	
	return markets

		
if __name__ == "__main__":
	main()
