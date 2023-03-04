import requests
import re
import json

def cloud_comment(id):
    url = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + str(id)
    res = requests.get(url)
    json_str_re = re.compile("{.*}",re.S)
    json_str = json_str_re.search(res.text).group()
    #print (json_str)
    comment_dict = json.loads(json_str)
    #print (comment_dict)
    num = 0
    for comment in comment_dict["hotComments"]:
        print ("热评" + str(num) + ":" + comment["content"].replace("\n",""))
        num = num+1

if __name__ == '__main__':
    cloud_comment(1491714569)
