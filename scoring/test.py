import requests

requests.post(
   "http://127.0.0.1:3000/predict",
   headers={"content-type": "application/json"},
   data="[[0.76, 45, 2, 0.8, 9000, 10, 0, 6, 0, 2]]",
).text