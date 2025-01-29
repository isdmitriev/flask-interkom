from flask import Flask, request, jsonify
from typing import Dict
import sys
import logging

app = Flask(__name__)


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    return logger


def handle_conversation_user_created(data):
    conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
    print(conversation_id)
    return jsonify({"status": "success", "message": "Webhook received"}), 200


def handle_conversation_user_replied(data):
    conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
    message: str = (
        data.get("data", {})
        .get("item", {})
        .get("conversation_message", {})
        .get("body", "")
    )
    print(f"{conversation_id}:{message}")
    return jsonify({"status": "success", "message": "Webhook received"}), 200


def handle_conversation_admin_replied(data):
    conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
    message: str = (
        data.get("data", {})
        .get("item", {})
        .get("conversation_message", {})
        .get("body", "")
    )
    print(f"{conversation_id}:{message}")
    return jsonify({"status": "success", "message": "Webhook received"}), 200


def handle_conversation_admin_noted(data):
    conversation_id: str = data.get("data", {}).get("item", {}).get("id", "")
    message: str = (
        data.get("data", {})
        .get("item", {})
        .get("conversation_message", {})
        .get("body", "")
    )
    print(f"{conversation_id}:{message}:note")
    return jsonify({"status": "success", "message": "Webhook received"}), 200


def handle_conversation_admin_assigned(data):
    print("admin assigned")
    return jsonify({"status": "success", "message": "Webhook received"}), 200


logger = setup_logger()


@app.route("/conversations/messages", methods=["POST"])
def webhook():
    if request.is_json == True:
        data: Dict = request.get_json()

        topic = data.get("topic", "")
        if topic == "conversation.user.created":
            return handle_conversation_user_created(data)

        elif topic == "conversation.user.replied":
            return handle_conversation_user_replied(data)

        elif topic == "conversation.admin.replied":
            return handle_conversation_admin_replied(data)

        elif topic == "conversation.admin.noted":
            return handle_conversation_admin_noted(data)
        elif topic == "conversation.admin.assigned":
            return handle_conversation_admin_assigned(data)

        else:
            return jsonify({"status": "success", "message": "Webhook received"}), 200

    else:
        return jsonify({"status": "error", "message": "Invalid request format"}), 400


@app.route("/")
def hello_world():
    logger.info("path requested")
    # put application's code here
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
