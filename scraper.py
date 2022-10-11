# created by Miguel Flores

import scrapetube as st
from random import randint
from pytube import YouTube

SORT = 'upload_date'
# RESULTS_TYPE = 'video'


# search_term = str(input("Enter a search term: "))
max_vid = int(input("Enter the maximum number of videos to scrape: "))

# videos = st.get_search(search_term, max_vid, randint(2,5), SORT)



"""
    in order to get the video's thumbnail:
    video['thumbnail']['thumbnails'][-1]['url']
    URL: https://www.youtube.com/watch?v=" + video['videoId']
"""

vids = st.get_channel(None,'https://www.youtube.com/c/JazBazPhilippines', max_vid, randint(2,5))

links = []

keywords = ["camera", "Camera", "Live", "live", "Street", "street"]

for video in vids:
    title = video['title']['runs'][0]['text'].split(' ')
    for word in keywords:
        if word in title:
            links.append("https://www.youtube.com/watch?v=" + video['videoId'])

for link in links:
    yt = YouTube(link)
    try:
        print("Trying to download: " + yt.title + "at " + link)
        yt.streams.filter(type='video', progressive="False").get_highest_resolution().download()
    except:
        print("Error downloading video, proceeding to the next one")

# yt = YouTube(links[0])
# print(yt.streams.filter(type='video', progressive="False").get_highest_resolution())