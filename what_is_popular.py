import os
from time import time

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET_KEY = "YOUR_OAUTH_KEY.json"


def get_service():
    """Get credentials and create api client instance."""
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_KEY, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


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


def get_statistics_video(service, id):
    """Getting statistics dictionary from current video."""
    return service.videos().list(part="statistics", id=id).execute()


def get_count_stats(stat, type):
    """Getting count stats data from current video."""
    if type in stat["items"][0]["statistics"].keys():
        return int(stat["items"][0]["statistics"][type])
    else:
        return 0


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    print("Hello what are we comparing today?")
    tags = get_tags_to_comparing()

    youtube = get_service()

    # Initialize required variables
    commentCount = dict()
    viewCount = dict()
    likeCount = dict()
    for tag in tags:
        commentCount[tag] = 0
        viewCount[tag] = 0
        likeCount[tag] = 0

    start = time()
    for tag in tags:
        response = (
            youtube.search()
            .list(part="snippet", maxResults="25", q=tag, type="video")
            .execute()
        )
        for video in response["items"]:
            stat = get_statistics_video(youtube, video["id"]["videoId"])

            commentCount[tag] += get_count_stats(stat, "commentCount")
            viewCount[tag] += get_count_stats(stat, "viewCount")
            likeCount[tag] += get_count_stats(stat, "likeCount")

            # Like current video).
            # like = youtube.videos().rate(
            #     id=video['id']['videoId'],
            #     rating="like",
            # ).execute()

    print(f"Time passed: {round(time()-start, 2)}")
    print("Compare the numbers, decide for yourself.")
    for tag in tags:
        print(
            f"{tag.capitalize()}:   Views: {viewCount[tag]}   "
            + f"Likes: {likeCount[tag]}   Comments: {commentCount[tag]}"
        )


if __name__ == "__main__":
    main()
