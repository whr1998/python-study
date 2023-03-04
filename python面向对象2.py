class People:
    def __init__(self,name,weight):
        
        self.name = name
        self.weight = weight

    def __str__(self):
        
        return "我的名字叫%s，体重是%.2f公斤" % (self.name,self.weight)
    
    def run(self):
        print("%s爱跑步，跑步锻炼身体"%self.name)
        self.weight -= 0.5
        
    def eat(self):
        print("%s是吃货" %self.name)
        self.weight += 1.0


xiaoming = People("小明",60)
xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = People("小美",45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
