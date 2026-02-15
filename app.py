from flask import Flask, request, jsonify
import yt_dlp
import os

# تحديث yt-dlp كل مرة يقلع السيرفر (مهم لتيك توك)
os.system("pip install -U yt-dlp")

app = Flask(__name__)

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/dc", methods=["GET"])
def download():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "No url provided"})

    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'format': 'best',
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

if __name__ == "__main__":
    app.run()
