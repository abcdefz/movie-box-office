# -*- coding: utf-8 -*-
"""
爬取结果处理 未完待续...
"""

__author__ = "abcdefz"
__version__ = 0.1

import json
from prettytable import PrettyTable

def json_handler():
	x = PrettyTable()
	x.field_names = ["时间", "排名", "标题", "实时票房(万)", "票房占比", "累计票房(万)", "排片占比", "上映天数"]
	with open("result.txt", "r") as f:
		for line in f.readlines():
			line_dict = json.loads(line)
			time_key = line_dict.keys()[0]
			movie_values = line_dict.values()[0]
			for movie in movie_values:
				if len(movie) == 8: movie.pop()
				movie.insert(0, time_key)
				x.add_row(movie)
	print x

if __name__ == '__main__':
	json_handler()