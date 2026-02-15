from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)   # ← هذا هو الحل

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/dc")
def download():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "No URL provided"})

    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info["url"]
            title = info.get("title", "video")

        return jsonify({
            "title": title,
            "url": video_url
        })

    except Exception as e:
        return jsonify({"error": str(e)})
        
app.run(host="0.0.0.0", port=10000)
