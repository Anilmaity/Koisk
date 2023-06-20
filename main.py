import requests

url = "http://example.com/items/images/"
payload = {
    "prompt": "Cinematic Portrait, GodlyBeautiful french supermodel, dynamic lighting, [light + space of James Turrell + Bauhaus architectural forms], BeautyCore, Sharp Details --ar 21:9 --style raw"
}
headers = {
    'Authorization': 'Bearer <TokenID>',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)