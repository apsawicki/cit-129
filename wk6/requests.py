import requests
import json

req = requests.get("https://one.nhtsa.gov/webapi/api/Recalls/vehicle/modelyear/2000/make/saturn/model/ls?format=json")
# print(req.text)
# 200 = happy, 400 & 500 = not happy
if(int(req.status_code)) == 200:
    print(req.headers.keys())
apiDict = json.loads(req.text)
for x in apiDict:
    print(x, end='\n')
