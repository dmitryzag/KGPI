#Каталог

Как запустить проект:

python -m virtualenv venv \
. venv/bin/activate\
pip install -r requirements.txt \
sudo -u postgres psql -c "create user $(whoami);" \
sudo -u postgres psql -c "alter user $(whoami) createdb;" \
sudo -u postgres psql -c "create database django_db with owner $(whoami);" \
python3 manage.py runserver\

поменять в settings.py в DATABASES имя базы данных на Ваше
![image](https://user-images.githubusercontent.com/78315545/167538531-5cb6d5c4-94a5-4617-87a6-2420f0107783.png)
