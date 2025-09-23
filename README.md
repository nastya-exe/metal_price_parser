# Парсер + бот цены металлов: золото, серебро

### Структура:

#### Парсер:
- metal_price_parser.py - парсер (запуск от сюда)
- make_graph.py - построение графиков
- graphs - папка, куда сохраняется график

#### Бот:
- bot_parce.py - сам бот (запуск от сюда)
- keyboards.py - клавиатуры

#### Общее:
- bd_request.py - запросы к БД
- config.py - переменные
- db_price.db - бд с ценами за неделю

### Описание парсера:
metal_price_parser.py - при изменении цены на металл и в 23:00 добавляет новую цену в БД <br>
Функция start() запускает цикл, но работает только, если есть путь к БД. Для проверки парсера
запускать scrape_price_metal() <br><br>
make_graph.py - построение графиков для отправки в ТГ бот. Графики строятся на <br>
месяц, неделю, сегодняшний день

### Описание бота:
#### Две функции:
1. Получение текущего курса золота или серебра /price <br>
<img width="359" height="640" alt="image" src="https://github.com/user-attachments/assets/093a8eb9-e13f-424a-894a-2defe45afc5e" /><br>
2. Получение графиков за месяц, неделю, день /graph <br>
 <img width="359" height="640" alt="image" src="https://github.com/user-attachments/assets/ec95ad4c-19b7-4e64-bdd4-a3498f725755" /><br>

Графики с данными, полученные за неделю: <br>
<img width="2560" height="1536" alt="image" src="https://github.com/user-attachments/assets/7b2e178a-c0b8-4912-a418-79095a80a46e" /> <br>


<img width="2560" height="1536" alt="image" src="https://github.com/user-attachments/assets/6ecec02c-20aa-4de7-85e1-51f86eebbcba" />
