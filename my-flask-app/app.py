from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Render!"
    
@app.route("/1")
def f1():
    return render_template("1.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


