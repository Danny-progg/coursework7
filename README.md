В проекте реализована бэкенд-часть SPA веб-приложения для напоминания о выполнении привычек с помощью трекера в телеграмме. Телеграмм бот каждый раз будет присылать напоминание о выполнении привычки в определенное время, созданное пользователем. Программа помогает людям не забывать выполнять привычки, которые делают их жизнь лучше.

Для запуска программы нужно установить следующие пакеты: django django-rest-framework celery django_celery_beat django_cors_headers django-rest-framework-simplejwt drf_yasg eventlet(есть у вас Windows) psycopg2-binary pyTelegramBotAPI python-dotenv python-telegram-bot redis ..............

Для начала запуска проекта необходимо установить все пакеты и сохранить их в виртуальном окружении.

Для создания суперпользователя нужно в файле «.env_sample» ввести свои данные и ввести команду python manage.py csu

Для создания пользователей ввести команду python manage.py c_user и заполнить данные в терминале

Для создания базы данных в .env_sample введите свои данные. Далее в терминале введите: psql -U (имя пользователя ) -d (имя основной базы) и через команду create database (имя вашей базы); создайте базу данных.

Также ввести свой токен для телеграмм бота и id для чата в .env_sample. . Токен для телеграмм бота можно получить с помощью главного бота по этой ссылке: «https://t.me/BotFather».

Начните с ним диалог и выберите команду создания нового бота
BotFather предложит ввести имя вашего бота:здесь нужно указать видимое имя бота, т. е. то, которое отображается пользователям. Например, NameHabitBot.
После этого BotFather спросит юзернейм вашего бота. здесь бота нужно назвать уникально — это тот уникальный идентификатор, по которому бота можно будет найти. Также важно, чтобы имя заканчивалось на _bot.
Если имя подходит под все правила, BotFather предоставит токен и полезные ссылки для использования бота: Токен будет использован ботом для обращения к API Telegram-сервисов, поэтому его необходимо сразу сохранить и не распространять. Для получения id чата нужно найти в телеграмме бота под названием @getmyid_bot и в диалоге с ним нажать start/
Для запуска периодической задачи открыть два терминала и ввести следующие команды.

python.exe -m celery -A config worker -l INFO (-P eventlet "для Windows")
celery -A config beat -l info -s django

Запустить программу python manage.py runserver. Для запуска программы в docker-compose ввести команду docker compose up --build
