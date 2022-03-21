import random
import string
from hashlib import md5

import requests

url = "https://b2b-test2.alfastrah.ru/wapi/dictionary/vehicle/category"

request = requests.get(url)

nonce = request.headers["WWW-Authenticate"].split()[-1][7:71]
qop = request.headers["WWW-Authenticate"].split()[-2][5:9]
cnonce = "".join(random.choices(string.ascii_letters + string.digits, k=8))

str1 = "oocemb:alfastrah.ru:9W3DRUnV7tyXu47"
ha1 = md5(str1.encode("utf-8"))

str2 = "GET:https%3A%2F%2Fb2b%2Dtest2%2Ealfastrah%2Eru%2Fwapi%2Fdictionary%2Fvehicle%2Fcategory"
ha2 = md5(str2.encode("utf-8"))

str3 = f"{ha1.hexdigest()}:{nonce}:00000001:{cnonce}:{qop}:{ha2.hexdigest()}"
response = md5(str3.encode("utf-8"))

header = {
    "Authorization": 'Digest username="PO_AGENT", realm="alfastrah.ru", '
    + f"nonce={nonce}, uri={url}, cnonce={cnonce}, nc=00000001, "
    + f"qop=auth, response={response.hexdigest()}"
}

request = requests.get(url, headers=header)

print(request.status_code, request.headers)


# url = "https://b2b-test2.alfastrah.ru/wapi/dictionary/vehicle/category"
# header = {
#     "Authorization": "Bearer 726e182a-a227-3ba0-9ac0-07b488c9aba8",
#     "Content-Type": "application/json"
#     }
# request = requests.get(url, headers=header)
# pprint(request.json())
