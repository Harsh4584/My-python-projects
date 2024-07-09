from pytube import YouTube

link = "https://www.youtube.com/watch?v=Hw26a2AxbUo"
youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() #ye pure video audio sab kuch ke liye
# videos = youtube_1.streams.filter(only_audio=True) #ye only audio ke liye no video
V = list(enumerate(videos))
for i in V:
    print(i)
print()
strm = int(input("Enter: "))
videos[strm].download()
print("Succesfully Downloaded")

# For whole playlist download
# from pytube import Playlist

# py = Playlist("")# yaha playlist ka link dalna h

# print(f"Downloading : {py.title}")

# for video in py.videos:
#     video.streams.first().download()