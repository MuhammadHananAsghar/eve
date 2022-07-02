from flask import Flask, jsonify, request
from flask_cors import CORS
from youtube import Youtube

app = Flask(__name__)
CORS(app)
_youtube = Youtube()

@app.route("/")
def home():
    return jsonify({"home": "Youtube Scrape API by Muhammad Hanan Asghar"})

@app.route("/api", methods=['POST', 'GET'])
def api():
    query = request.args.get("query")
    response = _youtube.search(query)
    videos = _youtube.videos(response)
    return jsonify({"videos": videos})


if __name__ == "__main__":
    app.run(debug=True)