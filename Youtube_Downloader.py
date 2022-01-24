# pytube package
from pytube import YouTube
from pytube.streams import Stream 
#link of video
link = input("Enter Link: ")

def vid(link):
        video = YouTube(link)
        print(f"Video name: {video.title} \n ------------------------------------- \n ")
        for stream in video.streams.filter(progressive=True):
            print(stream)
        x = video.streams.get_by_itag(input("Enter tag: "))
        x.download(output_path="E:/")

vid(link)     
    



