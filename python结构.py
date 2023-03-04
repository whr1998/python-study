print ("---列表---")
list = ["路飞","索隆","娜美"]
print (len(list))
list.append("山治")
print (list)
list.insert(3,"乌索普")
print (list)
list.pop()
print (list)

print ("---元组---")
print ("类似列表的操作")
tuple = (1,2,3)
print (tuple)

print ("---字典---")
dict = {
        "name":"吴海荣",
        "age":23
        }

print (dict)
print (dict.values())
print (dict.keys())
print (dict.items())
