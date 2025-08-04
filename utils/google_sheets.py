import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "creds.json"
SHEET_NAME = "mega center vakansiya ruyxat"

def append_user_to_sheet(user_id: int, full_name: str, username: str):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([user_id, full_name, username or "", now])