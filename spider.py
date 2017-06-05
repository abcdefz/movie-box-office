# -*- coding: utf-8 -*-

__author__ = "abcdefz"
__version__ = 0.1

import requests
from scrapy.selector import Selector
import json
import datetime


def crawl():
	url = "http://www.cbooo.cn/"
	headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
	response = requests.get(url, headers=headers)
	return response.text

def get_data_from_response(html):
	tbody = Selector(text=html).xpath('//tbody[contains(@id, "topdatatr")]')
	tr_list = tbody.xpath("tr")
	result_list = []
	result_dict = {}
	for tr in tr_list:
		print tr.xpath("td/text()").extract()
		result_list.append(tr.xpath("td/text()").extract())

	time_key = datetime.datetime.now().strftime("%Y-%m-%d__%H:%M:%S")
	result_dict[time_key] = result_list
	
	with open("result.txt", "a+") as f:
		print >> f, json.dumps(result_dict)
	# print tr

def main():
	response = crawl()
	get_data_from_response(response)


if __name__ == '__main__':
	main()