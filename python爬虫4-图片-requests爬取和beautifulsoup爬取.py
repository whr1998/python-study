import requests
import re
from bs4 import BeautifulSoup

# def crawl_image(image_url,image_local_path):
#     r = requests.get(image_url,stream=True)
#     with open(image_local_path,"wb") as f:
#         f.write(r.content)

# def crwal():
#     url = "https://www.woyaogexing.com/tupian/dongman/2020/174287.html"
#     res = requests.get(url)
#     content_list = re.findall("<ul class=\"artCont cl\">.*?</ul>",res.content.decode("utf-8"),re.S)
#     for content in content_list:
#         image_list = re.findall("<p class=\"tx-img new_p\">.*?<img class=\"lazy\" src=\"(.*?)\"",content)
#         for image_url in image_list:
#             crawl_image("http:" + image_url,"./images/" + image_url.strip().split('/')[-1])

def crawl_image_bs4(image_url_bs4,image_local_path_bs4):
    r = requests.get(image_url_bs4,stream=True)
    with open(image_local_path_bs4,"wb") as f:
        f.write(r.content)
    
def crwal_bs4():
    url = "https://www.woyaogexing.com/tupian/weimei/2022/209869.html"
    res = requests.get(url)

    soup = BeautifulSoup(res.text,"html5lib")

    img_list = soup.find_all("ul",class_="artCont cl")
    for i in img_list:
        i = str(i)
        image_url = re.findall("<p.*?href=\"(.*?)\"",i)
        print (image_url)
        for i in image_url:
            crawl_image_bs4("http:" + i,"./images/" + i.strip().split('/')[-1])

if __name__ == '__main__':
    crwal_bs4()
