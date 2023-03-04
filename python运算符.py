a = 3
b = 2
list = [1,2,3]
print ("---算术运算符---")
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a**b)
print (a%b)
print ("---逻辑运算符---")
if a==3 and b==2:
    print ("and逻辑")
elif a==3 or b!=2:
    print ("or逻辑")
else:
    print (not a)
print ("---成员运算符---")
if b in list:
    print (list)
else:
    print (b + "not in list")
print ("---比较运算符---")
print (a>b)
print (a<b)
print (a!=b)
print ("---身份运算符 位运算符 赋值运算符---")
