# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20108610'))
    API_HASH = str(getenv('API_HASH', '262418f5ebe0a599821a5802a90ee1a5'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6590978998:AAFxHZcqaRmDUeZ64mk9pCYy-n08bYVyAtI'))
    name = str(getenv('name', 'sahoovpsbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '50'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002040564082'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '212.224.88.31'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "52014953230").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'gauravsahoo'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://mongodbuser:mogodbpass@cluster0.appjt7j.mongodb.net/'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Rk_botz'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'onepagelink.in')
    SHORTLINK_API = getenv('SHORTLINK_API', 'c47e1c4469c0a66e74af7153cb8f4d3b304d010')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/rk_back_up/18')
