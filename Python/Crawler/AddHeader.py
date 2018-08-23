# Evan
# Web Spider
import urllib.request
import urllib.parse
import json
import time
#reponse = urllib.request.urlopen('http://www.fishc.com')
#html = response.read().decode('utf-8')
#print(html)

# response = urllib.request.urlopen('https://placekitten.com/g/200/300')
# cat_img = response.read()
# with open('cat_img_200_300.jpg','wb') as f:
# 	f.write(cat_img)
'''
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
	'''
while True:

	content = input("请输入要翻译的内容(Press Q to quit)：")
	if content == 'Q':
		break
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	data={}
	data['i'] = content
	data['from']= 'AUTO'
	data['to']= 'AUTO'
	data['smartresult']= 'dict'
	data['client']= 'fanyideskweb'
	data['salt']= '1533881735900'
	data['sign']= '29a59b0cb1d76d79c34de453293f9461'
	data['doctype']= 'json'
	data['version']= '2.1'
	data['keyfrom']= 'fanyi.web'
	data['action']= 'FY_BY_CLICKBUTTION'
	data['typoResult']= 'false'
	data = urllib.parse.urlencode(data).encode('utf-8')

	request = urllib.request.Request(url,data)

	request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')

	response = urllib.request.urlopen(request)
	html = response.read().decode('utf-8')
	target = json.loads(html)
	#print(html)
	print('The result is: %s' % (target['translateResult'][0][0]['tgt']))
	time.sleep(3)