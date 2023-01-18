# DjangoReactTemplate

 The main goal of this project is to have a simple Django and React environment, with login, logout, registration, token authorization, etc...


# Dependencies

 Install the dependencies bellow before run Django

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install pillow
```
 
## Run Django :feelsgood:

```bash
cd app
python3 \manage.py makemigrations
python3 \manage.py migrate
python3 \manage.py runserver
```

## Start react to development

```bash
cd app/frontend/
npm install
npm run dev
```