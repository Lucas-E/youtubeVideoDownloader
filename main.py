from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}

def downloadVideo(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
