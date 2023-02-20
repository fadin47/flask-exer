from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

genre = ["action,", "mystery", "thriller", "horror", "comedy"]

user = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        orginazation = request.form.get("orginazation")
        user[name] = orginazation
        example = request.form["num"]
    return render_template("index3.html")

    
@app.route("/result3", methods=["GET", "POST"])
def result():    
    return render_template("result3.html", result=result)


if __name__ == "__main__":
        app.run(debug=True)