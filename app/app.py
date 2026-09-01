from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        message="Hello from GCP Kubernetes CI/CD Lab",
        version="v2"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/version")
def version():
    return jsonify(version="v2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
