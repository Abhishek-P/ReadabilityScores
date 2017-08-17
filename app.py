from flask import Flask, request, Response
import multiprocessing as mp
import json
encode = json.JSONEncoder().encode
app = Flask(__name__, static_url_path="")
text = ""
#pool1 = mp.Pool(5)

@app.route("/set", methods=["POST"])
def put():
    text = request.args["text"]
    return Response(encode({"code": "200", "message":"success"}), mimetype='text/json')

@app.route("/stats", methods = ["GET"])
def get():
    return "Ha!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)