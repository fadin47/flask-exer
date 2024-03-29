from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index2.html")


    
@app.route("/result2")
def result():    
    try:
        num = int(request.args.get("num"))
        if num % 2 == 0:
            result = f"{num} is even"
        else:
            result = f"{num} is odd"
    except (TypeError, ValueError):
        result = "not an integer"
    return render_template("result2.html", result=result)

if __name__ == "__main__":
        app.run(debug=True)