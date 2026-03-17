from flask import Flask, render_template, request, jsonify
from db import get_connFunc

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

# 전체 직원 조회
@app.get("/api/jikwon")
def jikwon_list():
    sql = """
        select jikwonno,jikwonname,busername,jikwonjik,jikwonpay,year(jikwonibsail) as ibsayear
        from jikwon
        inner join buser on jikwon.busernum = buser.buserno
        order by jikwonno
    """
    try:
        with get_connFunc() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
        return jsonify({"ok":True, "data":rows})
    except Exception as e:
        return jsonify({"ok":False, "error":str(e)}), 500

# 직원 1명 조회
@app.get("/api/jikwon/<int:jikwonno>")
def jikwon_one(jikwonno):
    sql = """
        select jikwonno,jikwonname,busername,jikwonjik,jikwonpay,year(jikwonibsail) as ibsayear
        from jikwon
        inner join buser on jikwon.busernum = buser.buserno
        where jikwonno = %s
    """
    try:
        with get_connFunc() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (jikwonno,))
                rows = cur.fetchall()
        return jsonify({"ok":True, "data":rows})
    except Exception as e:
        return jsonify({"ok":False, "error":str(e)}), 500

# 부서 전체 조회
@app.get("/api/buser")
def buser_list():
    sql = "select * from buser order by buserno"
    try:
        with get_connFunc() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
        return jsonify({"ok":True, "data":rows})
    except Exception as e:
        return jsonify({"ok":False, "error":str(e)}), 500

# 특정 부서 직원 조회
@app.get("/api/buser/<int:buserno>/jikwon")
def buser_jikwon(buserno):
    sql = """
        select jikwonno,jikwonname,busername,jikwonjik,jikwonpay,year(jikwonibsail) as ibsayear
        from jikwon
        inner join buser on jikwon.busernum = buser.buserno
        where jikwon.busernum = %s
        order by jikwonno
    """
    try:
        with get_connFunc() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (buserno,))
                rows = cur.fetchall()
        return jsonify({"ok":True, "data":rows})
    except Exception as e:
        return jsonify({"ok":False, "error":str(e)}), 500

if __name__=="__main__":
    app.run(debug=True)