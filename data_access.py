import sqlite3
import os
DB = None


def init():
    if os.environ.get("DB_READY"):
        return True

    else:
        try:
            open("test.db", "rb").close()
            global DB
            DB = sqlite3.connect("test.db")
            DB.execute('''CREATE TABLE REQUESTS  
                       ( req_id INT PRIMARY KEY NOT NULL
                       text TEXT NOT NULL,
                       scores TEXT);''')
            os.environ["DB_READY"] = True
            return True

        except Exception as ex:
            print ex
            return False


def add_new_request(req_id, text):
    try:
        DB.execute("INSERT INTO REQUESTS(req_id,text) VALUES (?,?);"(req_id, text))
    except Exception as ex:
        print ex

def set_scores(req_id,scores):
    try:
        DB.execute("INSERT INTO REQUESTS(scores) VALUES (?) WHERE req_id LIKE ? ", (req_id, scores))
    except Exception as ex:
        print ex
