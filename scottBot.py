import requests
import json
import sys



def main():
	url = "https://bittrex.com/api/v1.1/public/getmarkets"
	marketsummaries = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
	orderBook = "https://bittrex.com/api/v1.1/public/getorderbook?market={0}&type=both" 
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(marketsummaries)
	data = response.json()
	numMarkets = len(data["result"])
	
	#print(numMarkets)
	for i in range(0,numMarkets-1):
		name = data["result"][i]["MarketName"]
		tempUrl = orderBook.format(name)
		resp = requests.get(tempUrl)
		d = resp.json()
		brez = d["result"]["buy"]
		srez = d["result"]["sell"]
		if(brez is not None):
			buyResult = brez[0]["Rate"]
		if( srez is not None):
			sellResult = srez[0]["Rate"]
		#print("Market: {0} buy: {1}".format(name,len(d["result"]["buy"])))
		if((brez is not None) and (srez is not None)):
			print("Market: {0} buyRate: {1} sellRate: {2}".format(name, '{0:.16f}'.format(buyResult),'{0:.16f}'.format(sellResult)))
		#print(orderBook.format(name))
		#print(data["result"][i]["MarketName"])	
	
if __name__ == "__main__":
	main()
