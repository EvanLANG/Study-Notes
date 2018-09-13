# Practice with Requests and BeautifulSoup

import os
import requests
import time
from bs4 import BeautifulSoup

def download(url):
# for download page
    print("Getting page...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    req = requests.get(url, headers=headers)
    req.encoding = 'gb2312'
    print("Got!!!")
    return req.text
    
def get_plist(html):
# get the picture list
    soup = BeautifulSoup(html, 'html.parser')
    pic_list = soup.find_all('li', class_='wp-item')
    for item in pic_list:
        tag_a = item.find('h3', class_='tit').find('a')
        link = tag_a.get('href')
        text = tag_a.get_text()
        print('download {} and save'.format(text))
        get_pic(link, text)
        
def get_pic(link, text):
# get current picture and save
    html = download(link)
    soup = BeautifulSoup(html, 'html.parser')
    pic_list = soup.find('div', id='picture').find_all('img')
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    create_folder('Picture/{}'.format(text))
    for item in pic_list:
        src_link = item.get('src')
        req = requests.get(src_link, headers=headers)
        with open('Picture/{}/{}'.format(text, src_link.split('/')[-1]),'wb') as f:
            print('Saved picture {}'.format(src_link.split('/')[-1]))
            f.write(req.content)
            time.sleep(1)
            
def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
        
def execute(url):
    html = download(url)
    get_plist(html)
    
def main():
    create_folder('Picture')
    print('Starting create folder:')
    #queue = [i for i in range(1,7)] page number
    queue = [i for i in range(1,2)]
    for i in queue:
        cur_page = i
        #url = 'http://www.meizitu.com/a/legs_{}.html'.format(cur_page)
        url = 'http://www.meizitu.com/a/xxx_{}.html'.format(cur_page)
        print('Downloading page {}'.format(cur_page))
        execute(url)
        

            
            
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
