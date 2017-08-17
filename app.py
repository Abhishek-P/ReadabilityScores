from flask import Flask, request, Response
import multiprocessing as mp
import json
import text_statistics as ts
encode = json.JSONEncoder().encode
app = Flask(__name__, static_url_path="")
text = ""
pool1 = None
pool_result = None

def start_pool():
    global pool1
    if not pool1:
        pool1 = mp.Pool(1)
    return pool1

@app.route("/set", methods=["POST"])
def put():
    global pool1
    global pool_result
    text = request.args["text"]
    pool1 = start_pool()
    pool_result = pool1.apply_async(ts.Text, [request.args["text"]])
    return Response(encode({"code": "200", "message": "success"}), mimetype='text/json')

@app.route("/get/stats", methods = ["GET"])
def get_stats():
    if not pool_result:
        return Response(encode({"code": "200", "message": "Please post text first at /set as args"}), mimetype="text/json")
    if not pool_result.ready():
        return Response(encode({"code": "200", "message": "still processing try again"}), mimetype="text/json")

    else:
        return Response(encode({"code": "200", "message":pool_result.get().stats}))



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
