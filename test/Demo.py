import requests
import json

data = {
 "clientname":"SJNS2SC5",
 "clientId":"webapi",
 "Workflow":"signon",
 "szSignOnName":"9999",
 "szSignOnPassword":"9999"
}

headers = {'Content-Type': 'application/json;charset=utf-8'}

res = requests.post("http:// 10.1.22.7:9221/tpdotnet/pos/webapi/signon", json=data, headers=headers)

print(res.text)
