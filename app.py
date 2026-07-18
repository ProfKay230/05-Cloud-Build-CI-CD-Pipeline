from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>ProfKay CI/CD Demo</h1>
    <p>Automatically deployed using Cloud Build.</p>
    <p>Project 05 - Cloud Build CI/CD</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
