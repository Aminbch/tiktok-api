from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "TikTok Downloader API Running"

@app.route("/download")
def download():
    url = request.args.get("url")

    if not url:
        return jsonify({"error":"no url"})

    api = "https://www.tikwm.com/api/"
    r = requests.post(api, data={"url":url})
    data = r.json()

    if "data" in data and "play" in data["data"]:
        return jsonify({"video": data["data"]["play"]})
    else:
        return jsonify({"error":"not found"})

if __name__ == "__main__":
    app.run()
