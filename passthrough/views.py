from django.shortcuts import render
import yaml

import requests

# Create your views here.

config = yaml.load("config.yaml")
common_url = config['baseAPIRoute']

def invalid_response(errMsg, code=400):
  return JsonResponse({'error': errMsg}, code)

def get_prices(request):
  if request.method != "GET":
    return invalid_response("Invalid Method")

  requested_time = request.GET.get('requestedTime', None)
  site_id = request.GET.get('siteId', None)

  if (requested_time is None or site_id is None):
    return invalid_response("Missing 'requestedTime' and/or 'siteId' query parameters")

  url = common_url + config['urls']['getPrices']

  payload=f'Site_ID={site_id}&Requested_Time={requested_time}'
  headers = {}

  response = requests.get(url, headers=headers, data=payload, auth=(config["username"], config['password']), verify='client.pem')

  print(response)

  return JsonResponse({ 'data': 'nice' })