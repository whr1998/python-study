f = open("test2.txt")
lines = f.readlines()
count = {}
for line in lines:
    words = line.strip().split(' ')
    for word in words:
        if word not in count:
            count[word] = 0
        count[word] += 1
for i in count:
    print (i,count[i])
f.close()
