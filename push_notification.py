import os
import sys

import requests


def send_notification(message):
    api_key = os.environ.get("NOTIFYX_API_KEY")
    if not api_key:
        return "NotifyX: NOTIFYX_API_KEY is not configured."

    url = f"https://www.notifyx.cn/api/v1/send/{api_key}"
    data = {
        "title": "皎月连签到",
        "content": message,
    }

    response = requests.post(url, json=data, timeout=30)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        checkin_message = sys.argv[1]
        print(send_notification(checkin_message))
    else:
        print("Usage: python push_notification.py <checkin_message>")
        sys.exit(1)
