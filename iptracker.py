import requests

def track_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    print("IP Address: ", data['query'])
    print("Country: ", data['country'])
    print("City: ", data['city'])
    print("ISP: ", data['isp'])

ip_address = "8.8.8.8"  # Hier die IP-Adresse einfügen, die du verfolgen möchtest
track_ip(ip_address)
