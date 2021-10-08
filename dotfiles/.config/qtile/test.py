from funct import *
def get_ip():
    ip = requests.get("http://ipecho.net/plain?",timeout=1.0).text
    print(ip)

get_ip()
