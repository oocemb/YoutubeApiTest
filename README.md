[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# What is more popular on Youtube?

1) Youtube Data API v3
2) 52 requests (2 search, 50 statistics)
3) Pip packages

    pip install google-api-python-client oauth2client

    pip install google-auth-oauthlib google-auth-httplib2

4) no db
5) script
6) sync and async
7) 10 hours

Get started sync:

1) Google dev console
    
    Add Youtube Api 
    
    Create OAuth credentials, download key.json

2) Paste your key in 'CLIENT_SECRET_FILE' 
(the key must be in the file directory)

3) Install pip packages
4) Run and enter tags

    python what_is_popular.py
    
    ![](https://github.com/oocemb/YoutubeApiTest/blob/main/readme_image/create_tags.jpg)
    
5) Auth your Google account by link
    
    Copy paste authorization code
    ![](https://github.com/oocemb/YoutubeApiTest/blob/main/readme_image/credentials.jpg)
6) Compare and enjoy
    ![](https://github.com/oocemb/YoutubeApiTest/blob/main/readme_image/result.jpg)
    

Get started async:

1) Google dev console
    
    Add Youtube Api 
    
    Create default API key credentials, download key.json

2) Paste your key.json file in the file directory

3) Install pip packages (add aioyoutube)

    pip install aioyoutube

4) Run and enter tags

    python what_is_popular.py
    
    ![](https://github.com/oocemb/YoutubeApiTest/blob/main/readme_image/async_result.jpg)
    
6) Compare and enjoy
