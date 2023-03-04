import requests
import json

#获取某首歌的热评
def parse_index_comment():
    session = requests.Session()

    comment_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    
    headers = {
        
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'    
    }

    data = {
        'params': 'TfpEgNKjga/M3yaWROwciB/PB0leriRhWVsIo0mt5urKgLeGz/a19kdHehI/6ldjwsvOoa92zMEXJMMv9W//E6IcpLGjqCJUvwzfc6HizC+8b0rlSmBVv9uFoZE+OBw1GTP0196YKeq2IekaOTjMFXZrLAqUbW83TazvlMGhA8mz+jtRrTO5yqHHFCCQmRZUtic740BkzfxKiXb3jLmQxZMIwWLJ3Xvn9Yr7wkDZHtjmqF1OMUjQqw+L2TUnf+dCwVKsWuo3fAeUO7Bh0BsYLkWWheinT3vUNzAd++iNQZo=',
        'encSecKey': 'd8a798e1801c04b9ebd8d6a4e7588e75da0bdbf25595a885b0d5ef24dda18cc819c42ba09053b9fea64be34107e227536aa2382d7b71828a66705de0e25543cfae87b6240ef83c13465ab795da2ec8e087222c591cabb3924ff447c62ee925c581cee35095d9abc10be7dd0316d35904a0cd72c1095f2441682d1963f6052eea'
        
    }

    resp = session.post(url=comment_url,data=data,headers=headers)

    data = json.loads(resp.content)
    
    data = data['data']['hotComments']
    for i in data:
        showstr = i['user']['nickname'] + ':' + i['content']
        print(showstr)


    
if __name__ == '__main__':
    parse_index_comment()
