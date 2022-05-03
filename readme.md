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