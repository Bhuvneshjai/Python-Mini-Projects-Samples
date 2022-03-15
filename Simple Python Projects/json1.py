import json
a = {"name":"bhuvnesh","salary":600000,"langauge":"Python"}
# python dictionary convert into json variable by using dumps() function
b = json.dumps(a)
print(b)

data = '{"var":"bhuvnesh","var2":42}'
print(data)
# convert json varibale into python dictionary using loads function
parsed = json.loads(data)
print(type(parsed))

data1 = {
    "channel_name":"BhuviWorld",
    "cars":["BMW","AUDI 8","Ferrari"],
    "fridge":('roti',540),
    "isbad":False
}
print(data1)
# convert python dictionary into json variable using dumps function
jscomp = json.dumps(data1)
print(jscomp)