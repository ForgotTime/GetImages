from spider import *
from url import *
print('''
1.自动爬图
2.手动爬图
''')
#number = input("请输入：").strip()
number = "1"
if number == "1":
    pass
    url = get_random_url()
    get_page(url)
elif number == "2":
    pass
    url = input("请输入新浪网址：\n").strip()
    get_page(url)
