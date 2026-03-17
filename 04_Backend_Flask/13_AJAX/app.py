from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/friend")
def api_friendFunc():
    name = request.args.get("name", "").strip()
    # 1. 변수명을 처음부터 age_str로 명확히 받습니다.
    age_str = request.args.get("age", "").strip()
    
    # 입력 검증
    if not name:
        return jsonify({"ok":False, "error":"name is required"}), 400
    
    # 2. age_str 변수를 사용해 숫자가 맞는지 확인합니다.
    if not age_str.isdigit():
        return jsonify({"ok":False, "error":"age must be a number"}), 400
    
    # 3. 불필요한 if문을 없애고, 문자열을 진짜 숫자(int)로 변환합니다.
    age = int(age_str)
    
    # 4. 이제 age는 숫자이므로 덧셈/나눗셈 등 수학 연산이 가능해집니다!
    age_group = f"{(age // 10) * 10}대"
    
    return jsonify({
        "ok":True,
        "name":name,
        "age":age,
        "age_group":age_group,
        "message":f"{name}님은 {age}살 {age_group}입니다"
    })


if __name__=="__main__":
    app.run(debug=True)