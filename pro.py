from flask import Flask, request, jsonify, render_template
import os
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('down.html')

def download_video(url, type, quality):
    ydl_opts = {
        'format': 'best' if type == 'video' else 'bestaudio',
        'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }] if type == 'audio' else []
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    type = data.get('type')
    quality = data.get('quality')

    if url and type and quality:
        try:
            download_video(url, type, quality)
            return jsonify(success=True, message="Download started!")
        except Exception as e:
            return jsonify(success=False, error=str(e))
    else:
        return jsonify(success=False, error="Missing parameters")

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True, host='0.0.0.0', port=5000)