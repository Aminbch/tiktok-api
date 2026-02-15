from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/download")
def download():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "No URL"}), 400

    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
        "format": "mp4"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info["url"]
            title = info.get("title", "video")

        r = requests.get(video_url, stream=True)

        return Response(
            r.iter_content(chunk_size=1024),
            content_type="video/mp4",
            headers={
                "Content-Disposition": f'attachment; filename="{title}.mp4"'
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)})
