import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    Message = None
    if cpu > 100 or mem > 80:
        Message = "CPU Percentage or Memory Usage is high"
    return render_template("index.html", cpu=cpu, mem=mem, message=Message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")