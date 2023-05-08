import requests
import sys
from lxml import etree
import os
def save(content):
    file = open("spider.html", "wb")
    file.write(content)
    file.close()

def get_pages(urls):
    results = []
    for url in urls:
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
        res = requests.get(url, headers=headers)
        html = etree.HTML(res.content)
        result = html.xpath('//section/figure/img/@data-src')
        if not result:
            result = html.xpath('//section/figure/img/@src')
        result = ["https:" + str(i) if "http" not in str(i) else str(i) for i in result]
        results += result
    number = 1
    os.system("rm -rf ./*.jpg")
    for url in results:
        print(url)
        res = requests.get(url, headers=headers)
        print("成功获取一张图片")
        file = open("img{}.jpg".format(number), "wb")
        file.write(res.content)
        file.close()
        number += 1
    print("图片获取完成")

def get_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.content)
    result = html.xpath('//section/figure/img/@data-src')
    if not result:
        result = html.xpath('//section/figure/img/@src')
    result = ["https:" + str(i) if "http" not in str(i) else str(i) for i in result]
    print(result)
    number = 1
    os.system("rm -rf ./*.jpg")
    for url in result:
        print(url)
        res = requests.get(url, headers=headers)
        print("成功获取一张图片")
        file = open("img{}.jpg".format(number), "wb")
        file.write(res.content)
        file.close()
        number += 1
    print("图片获取完成")
if __name__ == "__main__":
    url = "https://k.sina.cn/article_7060325135_p1a4d4030f00100i5gy.html?from=history"
    get_page(url)    
