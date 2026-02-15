from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/download")
def download():
    url = request.args.get("url")

    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'format': 'mp4',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']
            return jsonify({"video": video_url})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
