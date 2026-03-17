from flask import Flask, render_template, request, jsonify
from db import get_connFunc

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

# 전체 조회
@app.get("/api/sangdata")
def list_sangdata():
    sql = "select code, sang, su, dan from sangdata order by code asc"
    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return jsonify({"ok":True, "data":rows})



if __name__=="__main__":
    app.run(debug=True)