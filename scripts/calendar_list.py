# isort:skip_file
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))

from utils.google_api import get_calendar_service


def main():
    service = get_calendar_service()

    page_token = None

    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()

        for item in calendar_list["items"]:
            # print(item)
            print(item["summary"], item["id"])

        page_token = calendar_list.get("nextPageToken")

        if not page_token:
            break


if __name__ == "__main__":
    main()
