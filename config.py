import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('bot_token')
database_url = os.getenv('database_url')

url_gold = 'https://mfd.ru/centrobank/preciousmetals/'
url_silver = 'https://mfd.ru/centrobank/preciousmetals/?left=1&right=-1'
