import urllib.request
file = urllib.request.urlopen('http://www.baidu.com')
result = file.read()

fhandle = open("./1.html","wb")
fhandle.write(result)
fhandle.close()


#1.urllib.request 请求模块

#2. urllib.error 异常处理模块

#3. urllib.parse url 解析模块

#4. urllib.robotparser robots.txt 解析模块
