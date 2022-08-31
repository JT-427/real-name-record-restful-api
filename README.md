# Real Name Record Rest API
> 2021年，台灣疫情再次爆發，政府推出簡訊實聯制來追蹤人民的活動路徑，以便有人確診時，透過追蹤路徑來通知可能接觸者。
> 不過透過簡訊的方式來發訊息，需要一定的費用，即便台灣電信業者已將發送簡訊實聯制的費用降到很低，但政府的預算卻也即將見底，因此我希望試著透過網路的方式來發送實聯制，來降低支出成本。

## 使用方法
首先，每位國民都可以拿到一個屬於自己的QRCode，與2021年底推出的「數位新冠病毒健康證明」類似，當出入個場所時，出示QRCode給店家掃描，即可透過網路來發送蹤跡。

## Requirements
- python >= 3.8

## Datebase Design
![img](https://github.com/JT-427/real_name_record_rest_api/blob/master/db/real_name%20record.png)

***
### 產生QRCode
```py
import requests
url = ''
data = {
    'people_id':people_id
}
response = requests.post(url + "qrcodegen", data=data)
print(response.json())
print(response.status_code)
```

### 發送蹤跡
```py
import requests
url = ''
data = {
    'people_id':people_id,
    'place_id':place_id
}
response = requests.put(url + "trace", data=data)
print(response.json())
print(response.status_code)
```

***
### 專案開發期間
2022/1
