print ("---无参数---")
def hello():
    print ("hello")
hello()
print ("---有参数---")
def double(x):
    print (x**2)
double(3)
print ("---带默认参数---")
def hello(str = "hello"):
    print (str)
hello()
hello("hello world")
print ("---不定长参数---")
def print_hello(s,*arg):
    print (s)
    for a in arg:
        print (a)
print_hello("你好")
print_hello("hello","world!")


print ("---阶乘---")
def jiecheng(x):
    num = 1
    while x>0:
        num *= x
        x -= 1
    print (num)
jiecheng(5)
