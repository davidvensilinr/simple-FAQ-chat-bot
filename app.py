from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)

# Load intents from intents.json
with open("intents.json") as json_data:
    intents = json.load(json_data)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})


def get_response(user_input):
    user_input = user_input.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if user_input in pattern.lower():
                return random.choice(intent["responses"])

    return "I'm sorry, I didn't understand that."


if __name__ == "__main__":
    app.run(debug=True)
