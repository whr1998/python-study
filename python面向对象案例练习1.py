'''
面向对象案例：
	老张开车去东北
	案例分析：
	对象有：人
		交通工具
		地点				  
'''

class Person:

    def __init__(self,name):
        self.name = name

    def drive(self,tool,place):
        tool.driving()
        print("{}开{}去{}".format(self.name,tool.name,place.name))

class Traffic_Tools:

    def __init__(self,name):
        self.name = name

    def driving(self):
        print("{}已经启动".format(self.name))

class Place:

    def __init__(self,name):
        self.name = name

lz = Person("老张")
tool = Traffic_Tools("宝马")
place = Place("东北")

        
lz.drive(tool,place)
