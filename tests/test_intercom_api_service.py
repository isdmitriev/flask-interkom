from services.intercom_api_service import IntercomAPIService
from typing import Dict

CLIENT: IntercomAPIService = IntercomAPIService()


def test_get_admins():
    result = CLIENT.get_all_admins()
    status_code, data = result

    assert status_code == 200


def test_add_admin_message_to_conversation():
    admin_id: str = "8028082"
    conversation_id: str = "6"
    message: str = "i am Isdmitriev2@gmail.com"

    result = CLIENT.add_admin_message_to_conversation(
        admin_id=admin_id, conversation_id=conversation_id, message=message
    )
    assert result[0] == 200


def test_add_admin_note_to_conversation():
    admin_id: str = "8028082"
    conversation_id: str = "6"
    note: str = "note from Isdmitriev2@gmail.com"
    result = CLIENT.add_admin_note_to_conversation(
        conversation_id=conversation_id, note=note, admin_id=admin_id
    )
    assert result[0] == 200
