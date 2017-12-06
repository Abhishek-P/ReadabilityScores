from flask import Flask, request, Response, render_template
from werkzeug.contrib.fixers import ProxyFix
import multiprocessing as mp
import json
import text_statistics as ts
import os
import uuid
import data_access
ON_HEROKU = os.environ.get('ON_HEROKU')
if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 5000
encode = json.JSONEncoder().encode
app = Flask(__name__, static_url_path="")
text = ""
pool1 = None
pool_result = None


def start_pool():
    global pool1
    if not pool1:
        pool1 = mp.Pool(4)
    return pool1


@app.route("/")
def home():
    return render_template("rscores.html")


@app.route("/set", methods=["POST"])
def put():
    global pool1
    global pool_result
    text = request.form["text"]
    if not pool1:
        pool1 = start_pool()
    data_access.add_new_request(id,text)
    id = uuid.uuid4().__int__()

    pool_result = pool1.apply_async(ts.Text, [request.form["text"].encode('utf-8')])
    return Response(encode({"code": "200", "message": "success", "id": id}), mimetype='text/json')


def get_stats():
        return Response(encode({"code": "200", "message":pool_result.get().stats}))


def get_value(key):
    if key not in pool_result.get().stats :
        return Response(encode({"code": "200", "message": "No such stat"}), mimetype="text/json")

    else:
        return Response(encode({"code": "200", "value": pool_result.get().stats[key]}))


def get_object():
    return Response(encode({"code": "200", "value": json.dumps(pool_result.get(), default=lambda o: o.__dict__)}))


get_funcs = {"stats": get_stats, "stat": get_value }


@app.route("/get/<key>", methods = ["GET"])
def get(key):
    if not pool_result:
        return Response(encode({"code": "200", "message": "Please post text first at /set as args"}),
                        mimetype="text/json")
    if not pool_result.ready():
        return Response(encode({"code": "200", "message": "still processing try again"}), mimetype="text/json")

    if key == "stats":
        return get_funcs["stats"]()

    if key == "object":
        return get_object()

    else:
        return get_funcs["stat"](key)
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = port, debug=True)
