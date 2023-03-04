import re
import requests
import html
import time

def music_comment():
    url = "https://music.163.com/#/song?id=1436910205"
    res = requests.get(url)

    pattern = re.compile("<div class=\"cnt f-brk\">.*?</div>")
    body = html.unescape(res.text).replace("<br/>","\n")
    m = pattern.findall(body)

    comment_writer = re.compile("class=\"s-fc7\">(.*?)</a>")
    comment_content = re.compile("</a>(.*?)<a",re.S)

    f = open("爬虫输出2.txt","w")
    for comment in m:
        output  = []
        writer = comment_writer.findall(comment)
        if len(writer) > 0:
            output.append(writer[0])
        print("\t".join(output))
        content = comment_content.findall(comment)
        if len(content) > 0:
            output.append(content[0])
        print("\t".join(output))
        time.sleep(1)
        f.write("\n".join(output))
        f.write("\n")

    f.close()

if __name__ == '__main__':
    music_comment()
