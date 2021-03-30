from flask import Flask,request,redirect,render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/math2")
def calc_yen():
    hankei = float(request.args.get("hankei"))
    ensyu = float((hankei * 2)* 3.14)
    menseki = float(hankei * hankei * 3.14)
    return render_template("math2.html",ensyu=ensyu,menseki=menseki)

@app.route("/kyuyo")
def kyuyo():
    return render_template("salary.html")

@app.route("/result")
def result():
    time_money = int(request.args.get("time_money"))
    worktime = int(request.args.get("worktime"))

    salary = time_money * worktime * 31
	
    return render_template("salary_result.html",salary=salary)

if __name__ == "__main__":
    app.run(debug=True)