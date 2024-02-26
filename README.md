# Charon

Система ретрансляции сообщений в Телеграм с проверкой безопасности

Установка
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py crontab add
python manage.py runserver
```

Запрос на получение обновлений из Телеграма (забираем список чатов и подписчиков)
```
curl <host>:<port>/api/get_updates
```

Запрос на отправку сообщений
```
curl -H 'Token: <token>' '<host>:<port>/api/send_message?message=<message>'
```

PS: **Харон** в греческой мифологии — перевозчик душ умерших через реку Стикс