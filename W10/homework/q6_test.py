import requests
import time


url = "http://localhost:9696/predict"

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
while True:
    # time.sleep(0.0001)
    response = requests.post(url, json=client).json()
    print(response)
