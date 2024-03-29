import datetime

from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%A, %B %d %Y, %I:%M:%S %p")
    templateData = {
        'title': 'Current Date and Time',
        'time': timeString
    }
    return render_template('index1.html', current_time=timeString)

if __name__ == "__main__":
        app.run(debug=True)