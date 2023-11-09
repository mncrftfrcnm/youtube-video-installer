#install pytube!
from pytube import YouTube
link = input('link: ')
youtubeObject = YouTube(link)
youtubeObject = youtubeObject.streams.get_highest_resolution()
youtubeObject.download()
