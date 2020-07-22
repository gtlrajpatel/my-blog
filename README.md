# my-blog

**My Blog is a micro blogging application built with Django Framework.**

My Blog project is made up with both by using  REST Framework and without using  REST Framework.

# Installation steps



1> Clone the repository

```
git clone https://github.com/gtlrajpatel/my-blog.git
```

2> Create virtualenv

```
virtualenv -p python3.6 venv_myblog

source venv_myblog/bin/activate
```

3> Install dependencies

```
pip install -r requirements.txt
```

4> Create local.py file

```
cp my_blog/my_blog/settings/example-production.py my_blog/my_blog/settings/local.py
```

5> Run migrations (Go to `project root` folder)

```
python manage.py makemigrations
python manage.py migrate
```

6> Run the project

```
python manage.py runserver
```
<br/>

**My Blog project contains 3 apps.** 

1> blog (Non REST API App):

```
http://127.0.0.1:8000/
```

2> blog_api (REST API App)

```
http://127.0.0.1:8000/api/
```

3> users (Custom User Model)

Note: Both blog & blog_api apps are made independent in order to further development as separate projects. Both apps have their own separate models.
<br/><br/><br/>

* User has to register, verify & login himself/herself to read & create blogs. Although UI for that is pretty simple, but the urls are:

```
http://127.0.0.1:8000/accounts/signup/              (Registration for both app)

http://127.0.0.1:8000/accounts/login/               (For Non REST Login)

http://127.0.0.1:8000/api-auth/login/?next=/api/    (For REST API Login)
``` 
