#using proxy
import urllib.request
import random

#url = 'http://www.fishc.com'
url = 'https://www.whatismyip.com/'

iplist = ['219.141.153.39:80','219.141.153.35:80']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')]

urllib.request.install_opener(opener)
#opener.open(url)
response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
