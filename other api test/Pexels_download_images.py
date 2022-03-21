from pprint import pprint

import requests

PEXELS_API_KEY = "563492ad6f91700001000001e5f2cf95f0184911b01f9c4563cd1444"


def download(query: str, per_page: int):
    """Скачивает файл по передаваемому запросу"""
    URL = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
    header = {"Authorization": PEXELS_API_KEY}

    request = requests.get(URL, headers=header)
    print(request)
    if request.status_code == 200:
        print("success")

        datas = request.json()
        for data in datas["photos"]:
            img = requests.get(data["src"]["small"], headers=header)
            out = open(f"{data['alt']}.jpg", "wb")
            out.write(img.content)
            out.close()
    else:
        pprint(request.status_code, "\n", request.text)


def main():
    query = input("What image are you looking for?  ")
    per_page = input("How many images to find?  ")
    if per_page.isdigit():
        download(query, per_page)


main()
