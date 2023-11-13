import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к. отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('low', 'Топ дешёвых отелей'),
    ('high', 'Топ дорогих отелей'),
    ('custom', 'Пользовательская настройка поиска'),
    ('history', 'Показать историю запросов')
)

URL = 'https://hotels4.p.rapidapi.com/'
