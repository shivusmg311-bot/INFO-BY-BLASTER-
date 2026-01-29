from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    uid = request.args.get("uid", "Not provided")
    region = request.args.get("region", "IND")

    return jsonify({
        "status": "FF Info API Working",
        "uid": uid,
        "region": region,
        "example": "/?uid=123456789&region=IND"
    })

def handler(environ, start_response):
    return app(environ, start_response)
