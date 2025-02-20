import yt_dlp

def download_video(url):
    ydl_opts = {'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_video('https://www.youtube.com/shorts/7Qk9L_V527s')