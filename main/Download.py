from pytube import YouTube



# # <-----FOR DOWNLAODING THE PLAYLIST------->
# from pytube import Playlist
# playlist = Playlist("LINK OF THE PLAYLIST")
# for video in playlist:
#     video.streams.get_highest_resolution().download()
# # <---------------------------------------->

link = "https://youtu.be/0mCVpUDCkEk"
location="E:\VideosDownloadByMain.py"
yt= YouTube(link)


print("Title:",yt.title)
print("Views:",yt.views)

# yd=yt.streams.get_lowest_resolution()
# yd=yt.streams.get_highest_resolution()
# yd=yt.streams.get_by_resolution(resolution="360p")
str= "360p"
yd=yt.streams.get_by_resolution(resolution= str)

# <------------FOR ONLY AUDIO------------>
# yd=yt.streams.get_audio_only()
# <-------------------------------------->


# <  If you have not changed the path and downloading previously
# downloaded videos then old one will be replaced without any confirmation   >
yd.download(link)

print("Download Complete :)")
print("Location Of The Video Is: ",location)