#4.4
#列表、数组部分元素处理
players=['a','b','c','d','e','f']
print(players[0:3])  #列表、数组名[a:b]，选取其中索引为a至b-1的元素，忽略a则从头开始，忽略b则直到最后
print(players[-3:])  #特殊的， 列表、数组名[-c:]，选取最后c个元素
team=players[0:5]   #列表、数组复制，后面[]不可省略
team=players[:]
print(team)

#部分循环
for player in players[-3:]:
    print(player.title())