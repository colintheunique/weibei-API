# -*- coding: utf-8 -*-

import codecs
import webbrowser  
import json  
from weibo import APIClient  
import tablib
import time 
  
APP_KEY = '3652983772' # your app key  
APP_SECRET = 'c078482fa87384b227911961b2a4bfa3' # your app secrect  
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # your callback url  
  
client = APIClient(APP_KEY,APP_SECRET,CALLBACK_URL)  
  
# 访问授权页，让用户授权  
authorize_url = client.get_authorize_url(redirect_uri = CALLBACK_URL)  
  
#打开浏览器，需手动找到地址栏中URL里的code字段   
webbrowser.open(authorize_url)  
  
# 手动输入新浪返回的code  
code = raw_input("input the code: ").strip()  
  
# 获得用户授权  
request = client.request_access_token(code) # 请求access_token  
access_token = request.access_token  # 新浪返回的token，类似abc123xyz456  
expires_in = request.expires_in  # token过期的UNIX时间  
  
print 'Successfully get access_token:',access_token  
print 'Successfully get expires_in:',expires_in  
  
client.set_access_token(access_token, expires_in)  

# 保存文件地址  
fp = codecs.open('D:/Program Files/python/weibo.txt', 'w', 'utf-8')  

# 获得开始和结束的UNIX时间  
sttime = int(time.mktime(time.strptime('2015-05-19 00:00:00', '%Y-%m-%d %H:%M:%S')))
edtime = int(time.mktime(time.strptime('2015-05-19 23:59:59', '%Y-%m-%d %H:%M:%S')))

nearbyplaceweibo = client.place.nearby_timeline.get(lat= +39.905, long = +116.425, range = 11000, starttime = sttime, endtime = edtime)
print nearbyplaceweibo.total_number
n = 0
weibosnmuber = nearbyplaceweibo.total_number
counts = 50
pagecounts = weibosnmuber / counts + 1
print pagecounts

for i in range(1, pagecounts + 1):  
    print i
    statuses = client.place.nearby_timeline.get(lat= +39.905, long = +116.425, range = 11000, starttime = sttime, endtime = edtime, page = i, count = counts).statuses
    for status in statuses:
        print str(n) + ','+ status['id']
        for i in status['geo']['coordinates']:
            fp.write(str(i) + ',')
        fp.write(status['text'] + ',')
        fp.write(status['created_at']+ '\n')
        n = n + 1

  
