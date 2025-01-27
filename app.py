from flask import Flask, request, jsonify
from typing import Dict

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.is_json == True:
        data: Dict = request.get_json()
        topic = data.get("topic", "")
        if topic == "conversation.user.created":
            conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
            print(conversation_id)
        elif topic == "conversation.user.replied":
            conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
            message: str = (
                data.get("data", {})
                .get("item", {})
                .get("conversation_message", {})
                .get("body", "")
            )
        else:
            print("None")

        return jsonify({"status": "success", "message": "Webhook received"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid request format"}), 400


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


if __name__ == "__main__":
    app.run()
