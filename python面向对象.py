#创建类
class Human():
    taisheng = True
    #初始化实例
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.__age = age #双下划线表示私有
    #定义类方法
    def show(self):
        if self.sex == "man":
            print (self.name + " is " + self.__age + " years old" + ",he can run.")
        elif self.sex == "woman":
            print (self.name + " is " + self.__age + " years old" + ",she can run.")
    #通过get接口访问私有变量
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

#创建实例
h1 = Human("john","man","22")
h2 = Human("mary","woman","40")
#调用类方法
h1.show()
h2.show()
#私有变量的get set
print (h1.name + " is " + h1.get_age())
print (h2.name + " is " + h2.get_age())
h1.set_age("14")
h2.set_age("29")
print(h1.get_age())
print(h2.get_age())
#继承
#创建子类
class child(Human):
    def __init__(self,name,sex,age):
        super(child,self).__init__(name,sex,age)
    def isTalk(self):
        if int(self.get_age()) > 3:
            print(self.name + " can talk" )
        else:
            print(self.name + " can not talk")
child1 = child("tom","man","6")
child1.isTalk()

