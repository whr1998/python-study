a = 1
b = 0
c = 5
list = [1,3,5,7,9]
dict = [
    {
    "name":"吴海荣",
    "age":23,
    "birthplace":"揭阳"
    },
    {
    "name":"吴海杰",
    "age":21,
    "birthplace":"揭阳"
    },
    {
    "name":"李彩铃",
    "age":45,
    "birthplace":"揭阳"
    },
    {
    "name":"吴俊达",
    "age":48,
    "birthplace":"揭阳"
    }
]

if a:
    for i in list:
        print (i)
        if i == 5:
            break
if b==0:
    for i in dict:
        if i["age"] == 21:
            continue
        print (i)
for i in range(0,10):
    print (i)
while c>0:
    print (c)
    c-=1
    
