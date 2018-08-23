# Evan
# Web Spider
import urllib.request
import urllib.parse
import json
#reponse = urllib.request.urlopen('http://www.fishc.com')
#html = response.read().decode('utf-8')
#print(html)

# response = urllib.request.urlopen('https://placekitten.com/g/200/300')
# cat_img = response.read()
# with open('cat_img_200_300.jpg','wb') as f:
# 	f.write(cat_img)


content = input("请输入要翻译的内容：")
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

response = urllib.request.urlopen(url,data)

html = response.read().decode('utf-8')
target = json.loads(html)
#print(html)
print('The result is: %s' % (target['translateResult'][0][0]['tgt']))
