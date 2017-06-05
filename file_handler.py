# -*- coding: utf-8 -*-
"""
	email result.txt every night
	after that  clean result.txt
"""

__author__ = "abcdefz"
__version__ = 0.1


import os
import logging
import requests
import datetime

"""
使用 mailgun 发送邮件
"""
def send_email():
    sender = "我是票房爬虫 <EMAIL>"
    to = [
        "EMAIL"
    ]
    files = [("inline", open("result.txt", 'rb'))]
    title = "%s 爬取结果" % datetime.datetime.now().strftime("%Y-%m-%d")
    body = """
Have a nice night.
    """


    return requests.post(
        "Your own mailgun url",
        auth = ("api", "your own key"),
        files = files,
        data = {
            "from": sender,
            "to": to,
            "subject": title,
            "text": body,
        },
    )

def clean_file(file_name):
	if os.path.isfile(file_name):
		with open("result.txt", "w") as f:
			print >> f

if __name__ == '__main__':
	print send_email().text