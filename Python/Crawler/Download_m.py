import urllib.request
import os
import re

def url_open(url):
##    data = {}
##    data[':authority'] = 'zhihu-web-analytics.zhihu.com'
##    data[':method'] = 'POST'
##    data[':path'] = '/api/v1/logs/batch'
##    data[':scheme'] = 'https'
##    data['accept'] = '*/*'
##    data['accept-encoding'] = 'gzip, deflate, br'
##    data['accept-language'] = 'en,zh-CN;q=0.9,zh;q=0.8'
##    data['content-encoding'] = 'gzip'
##    data['content-length'] = '504'
##    data['content-type'] = 'application/x-protobuf'
##    data['origin'] = 'https://www.zhihu.com'
##    data['referer'] = 'https://www.zhihu.com/question/289015913'
##    data['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
##    data['x-za-batch-size'] = '1'
##    data['x-za-log-version'] = '2.3.91'
##    data['x-za-platform'] = '1'
##    data['x-za-product'] = '1'
##    data = urllib.parse.urlencode(data).encode('utf-8')
    
    req = urllib.request.Request(url,data)
 #   req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    #print(url)
    return html	

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a) 
    #print(html[a:b])
    return html[a:b]

def find_images(url):
    #print(url,'?????1')
    html = url_open(url).decode('utf-8')
    with open('tt.txt','w',encoding='utf-8') as f:
        f.write(html)
    #print(html)
    img_addrs = re.findall(r'data-original="https://pic.+?r\.jpg',html)
    print(len(img_addrs))
    return img_addrs
    #print(img_addrs[1:10])
##    a = html.find('img src=')
##    while a != -1:
##        b = html.find('.jpg',a,a+255)
##        if b != -1:
##            img_addrs.append(html[a+9:b+4])
##            print(html[a+9:b+4])
##        else:
##            b = a+9
##        a = html.find('img src=', b)
    #for each in img_addrs:
#        print(each)

def save_images(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each[15:])
            f.write(img)
        
def download_m(folder_name='jian_dan', pages=10):
#    os.mkdir(folder_name)
#    os.chdir(folder_name)

#    url = 'http://jandan.net/ooxx/'
    url = 'https://www.zhihu.com/question/289015913'
#    page_num = int(get_page(url))

    for i in range(pages):
#        page = page_num - i
#        page_url = url + 'page-' + str(page) + '#comments'
#        img_addrs = find_images('http://jandan.net/ooxx/page-42#comments')
        img_addrs = find_images(url)
#        save_images(folder_name,img_addrs)
        break

if __name__ == '__main__':
    download_m()
