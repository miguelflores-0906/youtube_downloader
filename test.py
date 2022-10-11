from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=7YEmt_5p-V4&t=23s")

yt.streams.filter(type='video', progressive="False").get_highest_resolution().download()