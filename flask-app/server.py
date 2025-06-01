from flask import Flask, request, jsonify
from src.tokenizer import tokenize

PORT = 5000

app = Flask(__name__)

@app.route("/flask", methods=["POST"])
def index():
    data = request.get_json()
    word_embeddings, positional_embeddings, final_embeddings = tokenize(data["text"])
    return jsonify(
        {
            "word_embeddings": word_embeddings.tolist(),
            "positional_embeddings": positional_embeddings.tolist(),
            "final_embeddings": final_embeddings.tolist(),
        }
    )


if __name__ == "main":
    app.run(port=PORT, debug=True)
