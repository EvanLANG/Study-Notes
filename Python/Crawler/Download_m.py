import urllib.request
import os
import re

def url_open(url):
    #can add proxy here
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
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
    html = url_open(url).decode('utf-8')
    with open('tt.txt','w',encoding='utf-8') as f:
        f.write(html)
    #print(html)
    img_addrs = re.findall(r'data-original="https://pic.+?r\.jpg',html)
    print(len(img_addrs))
    return img_addrs

def save_images(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each[15:])
            f.write(img)
        
def download_m(folder_name='jian_dan', pages=10):
    os.mkdir(folder_name)
    os.chdir(folder_name)

#    url = 'http://jandan.net/ooxx/'
    url = 'https://www.zhihu.com/question/xxxxxx'
#    page_num = int(get_page(url))

    for i in range(pages):
#        page = page_num - i
#        page_url = url + 'page-' + str(page) + '#comments'
#        img_addrs = find_images('http://jandan.net/ooxx/page-42#comments')
        img_addrs = find_images(url)
        save_images(folder_name,img_addrs)
        break

if __name__ == '__main__':
    download_m()
