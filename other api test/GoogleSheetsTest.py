import apiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

# https://developers.google.com/sheets/api/reference/rest
# Подготовка к работе:
# Открыть доступ к администратору google.console нужному файлу (service.acount)
# oocemb@buoyant-idea-344515.iam.gserviceaccount.com
# ключ api с google.console (активировать sheet, drive)
CREDENTIALS_FILE = "credential.json"
# https://docs.google.com/spreadsheets/d/1Yh7eWzIk40t4Oj4XyXuPpMNSybqNdvBZ67nOVIB0Tg8/edit#gid=0
# id из url нужной таблицы
spreadsheet_id = "1Yh7eWzIk40t4Oj4XyXuPpMNSybqNdvBZ67nOVIB0Tg8"

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

# values = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     range='A1:E10',
#     majorDimension='ROWS'
# ).execute()
# pprint(values)
# exit()


values = (
    service.spreadsheets()
    .values()
    .batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": "B3:C4",
                    "majorDimension": "ROWS",
                    "values": [
                        ["this is b3", "this is c3"],
                        ["this is b4", "this is c4"],
                    ],
                },
                {
                    "range": "D5:G4",
                    "majorDimension": "COLUMNS",
                    "values": [
                        ["this is d5", "this is d6"],
                        ["this is b4", "=6*6"],
                        ["7", "8"],
                        ["777"],
                    ],
                },
            ],
        },
    )
    .execute()
)
