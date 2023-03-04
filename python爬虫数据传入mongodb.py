import requests
import re
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cloud"]

mycol = mydb["comment"]

def comment(id):
    url = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + str(id)
    res = requests.get(url)
    json_str_re = re.compile("{.*}",re.S)
    json_str = json_str_re.search(res.text).group()
    #print(json_str)
    comment_dict = json.loads(json_str)

    comment_list = [comment_dict]
    x = mycol.insert_many(comment_list)

    print(x)

if __name__ == '__main__':
    comment(1491714569)
