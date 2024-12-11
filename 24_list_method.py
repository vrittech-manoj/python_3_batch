data = ["apple","ball","cat",5,9] #memory address 0xa3  ["apple","cat",5,9]
#print(data[0]) #output apple
# print(data.index("cat"))
# data.remove("ball")
# print(data)
# data.clear()
# print(data)
# second_list = []
# second_list = data.copy() #data
# print(second_list)
second_list = data # 0xa3  ["apple","ball","cat",5,9]
data.remove("ball")
print(second_list)