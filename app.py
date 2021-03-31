from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/en")
def keisan():
    hankei = request.args.get("hakei")
    ensyu = hankei * 6.28
    menseki = (hankei * hankei) * 3.14
    return render_template("circle.html", ensyu=ensyu, menseki=menseki)

@app.route("/kyuyo")
def kyuyo():
    jikyu = request.args.get("jikyu")
    jikyu = int(jikyu)
    jikan = request.args.get("jikan")
    jikan = int(jikan)

    kyuryo = jikyu * jikan
    return render_template("salary.html", salary=salary)

if __name__ == "__main__":
    app.run(debug=True)
