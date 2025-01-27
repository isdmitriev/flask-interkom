import requests


class IntercomAPIService:
    def __init__(self):
        self.access_token = (
            "dG9rOmVlNGY1MzhmXzNjNjNfNGZjOF9hNmFkX2JmZDgyNmNlZWRlYzoxOjA="
        )
        self.base_url = "https://api.intercom.io/"

    def get_all_admins(self):
        url: str = self.base_url + "admins"
        headers = {
            "Intercom-Version": "2.12",
            f"Authorization": f"Bearer {self.access_token}",
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.json())

    def create_admin(self, admin_email: str):
        url: str = self.base_url + "admins"
        headers = {
            "Content-Type": "application/json",
            "Intercom-Version": "2.12",
            f"Authorization": f"Bearer {self.access_token}",
        }

        payload = {"email": admin_email, "role": "operator", "name": "ilya"}
        response = requests.post(url, headers=headers, json=payload)
        print(response.status_code)
        print(response.json())

    def create_conversation(self, user_id: str, message: str):
        url: str = self.base_url + "conversations"
        headers = {
            "Content-Type": "application/json",
            "Intercom-Version": "2.12",
            f"Authorization": f"Bearer {self.access_token}",
        }
        payload = {"from": {"type": "user", "id": user_id}, "body": message}
        response = requests.post(url, headers=headers, json=payload)

    def attach_admin_to_conversation(self, admin_id: str, conversation_id: str):
        url = f"https://api.intercom.io/conversations/{conversation_id}/parts"
        headers = {
            "Content-Type": "application/json",
            "Intercom-Version": "2.12",
            f"Authorization": f"Bearer {self.access_token}",
        }
        payload = {"admin_id": admin_id, "message_type": "assignment", "type": "admin"}
        response = requests.post(url, headers=headers, json=payload)
        return response.json() if response.status_code == 200 else None

    def add_admin_note_to_conversation(
        self, conversation_id: str, admin_id: str, note: str
    ):
        url = f"https://api.intercom.io/conversations/{conversation_id}/reply"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = {
            "admin_id": admin_id,
            "type": "note",
            "message_type": "note",
            "body": note,
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response.status_code)

    def add_admin_message_to_conversation(
        self, conversation_id: str, admin_id: str, message: str
    ):
        url = f"https://api.intercom.io/conversations/{conversation_id}/reply"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        payload = {
            "admin_id": admin_id,
            "type": "note",
            "message_type": "comment",
            "body": message,
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response.status_code)

    def create_user(self, email: str):
        url: str = self.base_url + "contacts"
        headers = {
            "Content-Type": "application/json",
            "Intercom-Version": "2.12",
            f"Authorization": f"Bearer {self.access_token}",
        }
        payload = {"email": email}
        response = requests.post(url, headers=headers, json=payload)
        print(response.status_code)