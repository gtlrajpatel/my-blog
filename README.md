# my-blog

1> Clone the repository

```
git clone https://github.com/gtljaymodi/ride-sharing.git
```

2> Create virtualenv (We never commit virtualenv)

```
virtualenv -p python3.6 venv_ride_sharing

. venv_ride_sharing/bin/activate
```

3> Install dependencies

```
pip install -r requirements.txt
```

4> Create local.py file

```
cp ride_sharing/ride_sharing/settings/example-production.py ride_sharing/ride_sharing/settings/local.py
```

5> Run migrations (Go to `project root` folder)

```
python manage.py migrate
```

6> Run the project

```
python manage.py runserver
```