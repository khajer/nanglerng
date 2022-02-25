django-admin startproject nanglerng

python3 manage.py migrate

# install font awesome
pip3 install -r requirements.txt

# run server
python3 manage.py runserver
python3 manage.py runserver 8080

# create model
python3 manage.py startapp polls


# migrate database
python3 manage.py makemigrations nanglerng      // (Create the migrations)
python3 manage.py migrate nanglerng             // (execute the SQL commands). 


# admin 
python3 manage.py createsuperuser
admin
nanglerng0222
