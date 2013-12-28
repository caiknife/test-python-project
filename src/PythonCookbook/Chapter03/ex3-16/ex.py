#!/usr/bin/python
#/coding: UTF-8
'''
Created on 2012-11-17

@author: CaiKnife
'''

import httplib, smtplib

thresholdRate = 1.30
smtpServer = 'smtp.freebie.com'
fromAddr = 'foo@bar.com'
toAddrs = 'your@corp.com'

url = '/en/financial_markets/csv/exchange_eng.csv'
conn = httplib.HTTPConnection('www.bankofcanada.ca')
conn.request('GET', url)
response = conn.getresponse()
data = response.read()
start = data.index('United States Dollar')
line = data[start:data.index('\n', start)]
rate = line.split(',')[-1]
if float(rate) < thresholdRate:
    msg = 'Subject: Bank of Canada exchange rate alert %s' % rate
    server = smtplib.SMTP(smtpServer)
    server.sendmail(fromAddr, toAddrs, msg)
    server.quit()
conn.close()