import json
with open ('D:/Treinamento/python/miranda/abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    print(d1_json)

for k, v in d1_json.items():
    print(k, v)
    for k1, v1 in v.items():
        print(k1, v1)