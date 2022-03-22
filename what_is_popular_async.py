import asyncio
import json
from time import time

from aioyoutube import Api


# Initialize required variables
api = Api()
with open("api.json") as api_key:
    data = json.load(api_key)
    API_KEY = data["api"]

commentCount = dict()
viewCount = dict()
likeCount = dict()


def get_tags_to_comparing() -> list:
    """Receives a tag for comparing from the user."""
    while True:
        first_tag = input("First tag: ")
        if first_tag.isalpha():
            while True:
                second_tag = input("Second tag: ")
                if second_tag.isalpha():
                    break
                print("Tag only letters")
            break
        print("Tag only letters")
    return [first_tag.strip(), second_tag.strip()]


async def search_videos_by_tag(tag):
    return await api.search(key=API_KEY, text=tag), tag


def get_count_stats(stat, type):
    """Getting count stats data from current video."""
    if type in stat["items"][0]["statistics"].keys():
        return int(stat["items"][0]["statistics"][type])
    else:
        return 0


async def get_statistics_video(id: list):
    return await api.videos(key=API_KEY, part=["statistics"], video_ids=[id])


async def main():

    print("Hello what are we comparing today?")
    tags = get_tags_to_comparing()

    start = time()

    for tag in tags:
        commentCount[tag] = 0
        viewCount[tag] = 0
        likeCount[tag] = 0

    futures = [search_videos_by_tag(tag) for tag in tags]
    for future in asyncio.as_completed(futures):
        _list_id = []
        response, tag = await future
        for video in response["items"]:
            _list_id.append(video["id"]["videoId"])
        stats = [get_statistics_video(id) for id in _list_id]
        for stat in asyncio.as_completed(stats):
            result = await stat
            commentCount[tag] += get_count_stats(result, "commentCount")
            viewCount[tag] += get_count_stats(result, "viewCount")
            likeCount[tag] += get_count_stats(result, "likeCount")

    print(f"Time passed: {time()-start:0.2f}")
    print("Compare the numbers, decide for yourself.")
    for tag in tags:
        print(
            f"{tag.capitalize()}:   Views: {viewCount[tag]}   "
            + f"Likes: {likeCount[tag]}   Comments: {commentCount[tag]}"
        )


# only windows fix error
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
