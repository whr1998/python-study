print ("---写文件---")
f = open("test.txt","w")
f.write("写入write")
f.writelines(["写入writelines"])
f.close()

print ("---追加文件---")
f = open("test.txt","a")
f.write("追加write")
f.writelines(["追加writelines"])
f.close()

print ("---读文件---")
f = open("test.txt")
contenta = f.read()
print (contenta)
f.close()

print ("---读取大文件---")
f = open("test.txt")
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        print (line.strip())



