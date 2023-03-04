import re   #匹配字符串的模块，基于正则
import requests   #更简洁的http请求库
import html
import time
from bs4 import BeautifulSoup

def history_list_bybs4():
    #1.打开url
    url = "https://history.ifeng.com/"
    res = requests.get(url)

    #2.设置一个bs对象，参数为要解析的文本和解析器（html5lib等）
    soup = BeautifulSoup(res.text,"html5lib")

    #3.使用soup对象的find_all函数匹配文本
    history_list = soup.find_all("li",class_="news-stream-newsStream-news-item-has-image clearfix news_item")
    
    #4.输出title stripped_strings是获取html中的非标签字符串，自动去掉空白字符串
    for child in history_list:
        print("".join(child.find("h2",class_="news-stream-newsStream-mr13 news-stream-newsStream-news-item-title news-stream-newsStream-news-item-title-height").stripped_strings))
    time.sleep(1)


    
def history_list():
    #1.打开url
    url = "https://history.ifeng.com/"
    res = requests.get(url)

    #2.写正则匹配
    pattern = re.compile("<li class=\"news-stream-newsStream-news-item-has-image clearfix news_item.*?<a href.*?target=\"_blank\">.*?</li>",re.S)

    #对请求页面的处理-去掉转义字符以及替换字符
    body = html.unescape(res.text).replace("<br/>","\n")

    #3.根据正则表达式对获取的页面进行匹配
    m = pattern.findall(body)

    #2.写正则匹配
    title_pattern = re.compile("<h2 class=\"news-stream-newsStream-mr13 news-stream-newsStream-news-item-title news-stream-newsStream-news-item-title-height\">.*?target=\"_blank\">(.*?)</a>",re.S)

    f = open("爬虫输出1.txt","w")

    #输出匹配内容title
    for history in m:
        output = []
        title = title_pattern.findall(history)
        if len(title) > 0:
            output.append(title[0])
        print("\t".join(output))
        time.sleep(1)
        f.write("\n".join(output))
        f.write("\n")

    f.close()

#相当于c语言中的main函数，告知程序的起点
if __name__ == '__main__':
    history_list_bybs4()
