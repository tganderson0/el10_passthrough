import requests

url = "https://192.168.51.19:5000/eMosaicREST/site/GetPrice/"

payload={
  'Site_ID': 'USU',
  'Requested_Time': '2022-05-05T15:00:00.000Z'
}
headers = {}

username = 'USU'

response = requests.request("GET", url, headers=headers, data=payload, verify='client.pem')

print(response.text)
