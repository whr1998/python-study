import re

str = "abcdefg\nABCDEFG\n123\n?!.#\n \t "

m = re.findall(".",str)
print (m)

m = re.findall("[aA1!]",str)
print (m)

m = re.findall("\d",str)
print (m)

m = re.findall("\D",str)
print (m)

m = re.findall("\s",str)
print (m)

m = re.findall("\S",str)
print (m)

m = re.findall("\w",str)
print (m)

m = re.findall("\W",str)
print (m)

m = re.findall("abc",str,re.I)
print (m)

m = re.findall("a(.*)G",str,re.S)
print (m)

m = re.findall("a(.*)\n",str,re.I | re.S)
print (m)

m = re.findall("ab?",str,re.I)
print (m)

m = re.findall("\n+",str)
print (m)

p = re.compile("<div>(.*?)</div>")
m = p.findall("<div>HELLO</div>")
print (m)
m = p.findall("<div>WORLD</div>")
print (m)

p = re.compile("<div class='title'>.*?<h1>(.*?)</h1>")
str1 = "<div class='title'><h1>正在学正则表达式</h1></div>"
m = p.findall(str1)
print (m)
