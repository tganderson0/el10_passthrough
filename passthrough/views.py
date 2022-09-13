import json
from django.shortcuts import render
import yaml
from django.http import JsonResponse
import requests

# Create your views here.

with open("config.yaml", "r") as con:
  config = yaml.safe_load(con)


common_url = config['baseAPIRoute']

def invalid_response(errMsg):
  return JsonResponse({'error': errMsg})

def get_price(request):
  if request.method != "GET":
    return invalid_response("Invalid Method")

  requested_time = request.GET.get('Requested_Time', None)
  site_id = request.GET.get('Site_ID', None)

  if (requested_time is None or site_id is None):
    return invalid_response("Missing 'requestedTime' and/or 'siteId' query parameters")

  url = common_url + config['urls']['getPrice']

  payload = {
    'Site_ID': site_id,
    'Requested_Time': requested_time
  }
  headers = {'content-type': 'application/json', 'Accept': 'application/json'}

  response = requests.get(url, headers=headers, data=json.dumps(payload), auth=(config["username"], config['password']), verify='client.pem')

  print(response.text)

  return JsonResponse(json.loads(response.text))

def get_prices(request):
  if request.method != "GET":
    return invalid_response("Invalid Method")

  requested_time = request.GET.get('Requested_Time', None)
  site_id = request.GET.get('Site_ID', None)

  if (requested_time is None or site_id is None):
    return invalid_response("Missing 'requestedTime' and/or 'siteId' query parameters")

  url = common_url + config['urls']['getPrices']

  payload = {
    'Site_ID': site_id,
    'Requested_Time': requested_time
  }
  headers = {'content-type': 'application/json', 'Accept': 'application/json'}

  response = requests.get(url, headers=headers, data=json.dumps(payload), auth=(config["username"], config['password']), verify='client.pem')

  print(response.text)

  return JsonResponse(json.loads(response.text))

