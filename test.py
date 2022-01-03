import requests


data = {
    'people_id':'3dKSx0DLXak3JzaMfAGDnJg09zXlknJT',
    'place_id':'3IynHjTcmDLGdL75DLG1GXJm9A4ERqxsRF8EaigcacHVcdLE'
}
response = requests.put("http://127.0.0.1:5000/trace", data=data)
print(response.json())
print(response.status_code)


# =============================

'''
id = '3dKSx0DLXak3JzaMfAGDnJg09zXlknJT'
response = requests.post("http://127.0.0.1:5000/qrcodegen", data={'people_id':id})
print(response.json())
print(response.status_code)
'''

# =============================

'''
x = open("/Users/jt/Desktop/假個資.csv", mode="r")
x = x.readlines()
data = {}
for c, i in enumerate(x):
    if i.split(",")[0] != "":
        if i.split(",")[3] == '男性':
            gender = 'm'
        else:
            gender = 'f'

        data[i.split(",")[0]] = {
            'name':i.split(",")[1].rstrip(),
            'gender':gender,
            'contact_number':'0'+i.split(",")[2],
            'address':i.split(",")[4].replace("\n", "")
            }

for i in data:
    print(data[i])
    response = requests.put("http://127.0.0.1:5000/people", data=data[i])
    print(response.json())
    print("===============")
'''

# =============================

'''
x = open("/Users/jt/Desktop/假場景.csv", mode="r")
x = x.readlines()
data = {}
for c, i in enumerate(x):
    if i.split(",")[1] != '地點名稱' and i.split(",")[1] != '仁愛吾彊':
        data[c] = {
            'place_name':i.split(",")[1],
            'address':i.split(",")[2].replace("\n", "")
        }
for i in data:
    print(data[i])
        

for i in data:
    response = requests.put("http://127.0.0.1:5000/place", data=data[i])
    print(response.json())
    print("===============")
'''