## Постановка
Необходимо разработать HTTP API, с помощью которого можно:

- добавлять/удалять в хранилище информацию о городах;
- запрашивать информацию о городах из хранилища;
- по заданным широте и долготе точки выдавать 2 ближайших к ней города из присутствующих в хранилище.

При запросе к API на добавление нового города клиент указывает только название города, а в хранилище добавляются также координаты города. Данные о координатах можно получать из любого внешнего API.

Реализация хранилища произвольная.

***
#### Все задания выполнены

***
Для запуска необходимо установить все зависимости из requirements.txt
и ввести `uvicorn main:app --reload` (в режиме разработки).

***
Для подключения к mongodb:
Зарегистрироваться в облачном сервисе [MongoDB Atlas](https://www.mongodb.com/atlas/database).

(Для пользователей из России использовать VPN)

Создать файл.env и заполнить его в соответствии с .env.template.

Также для режима разработки: В разделе 'Network Access' указать IP Address - 0.0.0.0/0

***
Для просмотра результата:

http://127.0.0.1:8000/docs

***
## Requirements

+ Python 3.9.4
+ pymongo 4.3.3
+ motor 3.1.2
+ pydantic 1.10.7
+ fastapi 0.95.1
+ uvicorn 0.21.1
+ dnspython 2.3.0
+ python-dotenv 0.19.2
+ aiohttp 3.8.1
+ geopy 2.3.0