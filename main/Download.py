from pytube import Playlist
from pytube import YouTube

from pytube import Playlist
playlist = Playlist('https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&si=cC5KXqF27GIwP5fR')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    video=YouTube(video_url)
    try:
       #video.streams.first().download()
       video.streams.filter(res="720p").first().download()
    except:
         continue