import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from userbot.userbot import UserBot

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler('logs/userbot.log', when="midnight", encoding=None,
                                 delay=False, backupCount=10),
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

name = 'userbot'

# Read from config file
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

if bool(os.environ.get('ENV', False)):
    # Pyrogram details
    API_ID = os.environ.get('API_ID', None)
    API_HASH = os.environ.get('API_HASH', None)
    USERBOT_SESSION = os.environ.get('USERBOT_SESSION', None)

    # MongoDB details
    MONGO_URL = os.environ.get('MONGO_URL', False)
    DB_NAME = os.environ.get('DB_NAME', 'userbot')
else:
    # MongoDB details
    MONGO_URL = config.get('mongo', 'url')
    DB_NAME = config.get('mongo', 'db_name', fallback='userbot')
    DB_USERNAME = config.get('mongo', 'db_username')
    DB_PASSWORD = config.get('mongo', 'db_password')
    IS_ATLAS = config.getboolean('mongo', 'is_atlas', fallback=False)

# Extra details
__version__ = '0.2.0'
__author__ = 'athphane'

# Scheduler
scheduler = AsyncIOScheduler()

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()

UserBot = UserBot(name)
