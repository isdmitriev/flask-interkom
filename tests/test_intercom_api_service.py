from services.intercom_api_service import IntercomAPIService
from typing import Dict

CLIENT: IntercomAPIService = IntercomAPIService()


def test_get_admins():
    result = CLIENT.get_all_admins()
    status_code, data = result

    assert status_code == 200
