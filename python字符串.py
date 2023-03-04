s = "abcadeafg"
S = "ABCADEAFG"

print ("---查找---")
print (s.find("a"))
print (s.find("z"))

print ("---分割---")
print (s.split("a"))

print ("---大小写转换---")
print (s.upper())
print (S.lower())

print ("---切片---")
print (s[2:5])
print (s[:-1])

print ("---追加---")
print (s+S)

print ("---替换---")
print (s.replace("a","z"))

print ("---连接---")
print ("-".join(s))

print ("---反转---")
print (s[::-1])
