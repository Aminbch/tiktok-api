from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/download")
def download():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "no url"})

    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video = info["url"]
            title = info.get("title", "video")

        return jsonify({
            "title": title,
            "video": video
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()