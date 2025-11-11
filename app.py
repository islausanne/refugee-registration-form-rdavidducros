from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/records')
def records():
    return render_template("records.html")

@app.route('/refugees')
def refugees():
    return render_template("refugees.html")

if __name__ == '__main__':
    app.run(debug=True)
