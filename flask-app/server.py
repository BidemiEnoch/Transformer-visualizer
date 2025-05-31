from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/flask", methods=["POST"])
def index():
    data = request.get_json()
    print(data)
    return jsonify({"status":"Data acknowledged"})


if __name__ == "main":
    app.run(port=5000, debug=True)
