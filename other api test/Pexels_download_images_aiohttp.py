import aiohttp
import asyncio
import aiofile

from pprint import pprint


PEXELS_API_KEY = "563492ad6f91700001000001e5f2cf95f0184911b01f9c4563cd1444"
HEADER = {"Authorization": PEXELS_API_KEY}


async def get_data_list(query: str, per_page: int):
    """Getting dictionary data with urls and names images."""
    _URL = f"https://api.pexels.com/v1/search?query={query}&per_page={per_page}"
    async with aiohttp.request('GET', _URL, headers=HEADER) as response:
        if response.status == 200:
            data_list = dict()
            datas = await response.json()
            for data in datas["photos"]:
                data_list[data["src"]["small"]] = data["alt"]
        else:
            await pprint(response.status, "\n", response.text())
        return data_list


async def get_image_data_binary(url, header):
    async with aiohttp.request('GET', url, headers=header) as img_resp:
        return await img_resp.read(), url


async def create_image(binary_data, name):
    async with aiofile.async_open(f'{name}.jpg', 'wb') as afp:
        await afp.write(binary_data)


async def main():
    query = input("What image are you looking for?  ")
    per_page = input("How many images to find?  ") 
    data_list = await get_data_list(query, per_page)
    tasks_list = [get_image_data_binary(i,header=HEADER) for i in data_list.keys()]
    for future in asyncio.as_completed(tasks_list):
        binary_data, url = await future
        await create_image(binary_data, data_list[url])
        

# only windows fix error
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

asyncio.run(main())