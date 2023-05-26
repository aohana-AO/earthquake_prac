from django.test import TestCase
import requests
import json


url = "https://earthprac-json.up.railway.app/jsonget"
sess = requests.session()

print(sess.get(url))

csrftoken = sess.cookies['csrftoken']

# ヘッダ
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}

# 送信データ
prm = {
'type': 'eew', # 緊急地震速報の場合、String型のeewという文字列
'time': '1589131429000',
'report': '1', # 第一報の場合、String型の1という文字列。最終報はString型のfinalという文字列
'epicenter': '伊予灘', # 震源地
'depth': '60km', # 震源の深さ
'magnitude': 3.5, # 地震の規模を示すマグニチュード
'latitude': 33.8, # ここの２行はおそらく緯度経度的な
'longitude': 132.1,
'intensity': '2',
'index': 2
}

# JSON変換
params = json.dumps(prm)

# POST送信
res = sess.post(url, data=params, headers=headers)

# 戻り値を表示
print(json.loads(res.text))