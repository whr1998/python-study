class Student:

    count = 0
    
    def __init__(self,name):
        self.name = name
        Student.count += 1

    def learn(self):
        print("{}在学习".format(self.name))

xiaoming = Student("小明")
xiaohong = Student("小红")
xiaowang = Student("小王")
xiaoming.learn()
xiaohong.learn()
xiaowang.learn()

print("共有{}个学生在学习".format(Student.count))
