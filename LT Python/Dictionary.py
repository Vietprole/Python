cities = { 'Wales': 'Cardiff',
 'England': 'London',
 'Scotland': 'Edinburgh',
 'Northern Ireland': 'Belfast',
 'Ireland': 'Dublin'}
print(cities)

dic ={"Japan": "Osaka", "Korea": "Seoul"}
dic["Vietnam"] = "Hanoi" # Thêm phần tử
print(dic)

del dic["Korea"]
print(dic)

fruits = {"strawberry": "red", "peach": "pink", "banana": "yellow"}
for fruit, color in fruits.items():
    print(fruit + " is " + color)

fruits = {"strawberry": "red", "peach": "pink", "banana": "yellow"}
for fruit in fruits.keys(): # fruit là key
    print(fruit + " is " + fruits.get(fruit))

print('Wales' in cities)
print('France' not in cities)

