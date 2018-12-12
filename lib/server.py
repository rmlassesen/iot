from flask import Flask

app = Flask(__name__)

@app.route("/")
def ikea():
    return "IKEA Webpage"

@app.route("/mhs")
def mhs():
    return "Storage system"

def spin_up():
    print("Spinning up Storage server")
    app.run()
    return True