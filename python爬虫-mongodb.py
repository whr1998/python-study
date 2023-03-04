import pymongo

#创建数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["edu"]

#创建集合（也就是表）
mycol = mydb["student"]


#增
student_list = [
    { "sid":"0001","sname":"李华","sage":"18" },
    { "sid":"0002","sname":"伍佰","sage":"19" },
    { "sid":"0003","sname":"张强","sage":"17" },
    { "sid":"0004","sname":"刘应","sage":"17" },
    { "sid":"0005","sname":"李焕庆","sage":"20"}
]
x = mycol.insert_many(student_list)  
#还有insert_one
print(x)

#删
myquery = { "sid": "0002" }
y = mycol.delete_many(myquery)
print(y.deleted_count, "个文档已删除")
#还有delete_one

#改
myquery = { "sname": "刘应" }
newvalues = { "$set": { "sname": "卧槽" } }
mycol.update_many(myquery, newvalues)
#还有update_one

#查
for x in mycol.find():
  print(x)

#排序
mydoc = mycol.find().sort("alexa")
