#16.2
#利用urlopen下载数据
from __future__ import (absolute_import,division,print_function,unicode_literals)
try:
    from urllib2 import urlopen  #python2
except ImportError:
    from urllib.request import urlopen  #python3
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
#注意：该服务器id找不到，所以会报错
response = urlopen(json_url)  #打开网址
req = response.read()  #读取数据

with open('btc_close_2017_urllib.json','wb') as f:  #新建json文件
    f.write(req)  #写入

file_urllib = json.load(req)
print(file_urllib)

#使用requests扩展包使网络拉取数据简单化：
import requests
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)  #requests的get方法向服务器发送请求，并将返回结果存储在变量req中
with open('btc_close_2017_request.json，‘w') as f:
    f.write(req.text)  #.text属性直接读取文件数据，返回格式是字符串
    file_requests = req.json()  #.json将req中的文件数据转化成python列表file_requests