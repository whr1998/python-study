class HouseItem:

    def __init__(self,name,area):

        self.name = name
        self.area = area

    def __str__(self):

        return "家具名称：%s,家具占地面积：%.2f" %(self.name,self.area)


class House:

    def __init__(self,house_type,area):

        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n总面积：%s【剩余：%.2f】\n家具：%s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))

    def add_item(self,item):

        print("要添加%s" % item)

        if item.area > self.free_area:
            print("%s太大了" %item)
            return

        self.item_list.append(item.name)

        self.free_area -= item.area

bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("桌子",150)

print(bed)
print(chest)
print(table)

print("\n")

house1 = House("两房一厅",80)
house1.add_item(bed)
house1.add_item(chest)
house1.add_item(table)


print(house1)
