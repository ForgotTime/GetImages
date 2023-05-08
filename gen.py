import requests
import os
import lxml
import sys
def get_urls(baseurl):
    urls = []
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    res = requests.get(baseurl, headers=headers)
#print(res.json())
#sys.exit(0)
    contents = res.json()["data"]
    for content in contents:
        url = content["link"]
        print(url)
        urls.append(url)
    return urls
def get_urls_by_num(num):
    if not num >=1 and num <=92:
        return []
    author_id = "2161657"
    baseurl = "https://k.sina.cn/aj/newmedia/list?source=js&muid={}&pag                e={}".format(author_id, num)
    urls = get_urls(baseurl)
    return urls
def get_all_urls():
    urls = []
    for i in range(1, 93):
        urls += get_urls_by_num(i)
    return urls

if __name__ == "__main__":
    urls = get_all_urls()
    #urls = get_urls_by_num(1)
    file = open("urls.txt", "w")
    for url in urls:
        file.write(url+"\n")
    file.close()
    print("urls.txt文件生成完毕")
  
