from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("https://youtu.be/q8EevlEpQ2A?si=XOOPegkAiCVIltWa")
Download(link)
print('hello')