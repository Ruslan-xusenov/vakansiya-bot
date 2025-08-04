from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMINS: List[int] = [7528411248]

REQUIRED_CHANNELS: List[str] = ["@coder_babuin"]

DATA_DIR = "data/"
USERS_FILE = DATA_DIR + "users.json"
VACANCIES_FILE = DATA_DIR + "vacancies.json"
CITIES_FILE = DATA_DIR + "cities.json"
ADMINS_FILE = DATA_DIR + "admins.json"
CHANNELS_FILE = DATA_DIR + "channels.json"
