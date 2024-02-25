# Charon

Система ретрансляции сообщений в Телеграм с проверкой безопасности

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

PS: **Харон** в греческой мифологии — перевозчик душ умерших через реку Стикс