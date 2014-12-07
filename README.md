django-tornado
==============

An example how to run Django on Tornado. Simply run `run_tornado.py` and navigate your browser to

  [http://localhost:8080/hello-django](http://localhost:8080/hello-django)

or

  [http://localhost:8080/hello-tornado](http://localhost:8080/hello-tornado)

to see an HTTP-response from Django, respectively Tornado.

Settings
--------

You don't have to change anything to run this with your own Django project, but this line in `run_tornado.py`:

```python
os.environ['DJANGO_SETTINGS_MODULE'] = 'demosite.settings' # TODO: edit this
```

The `DJANGO_SETTINGS_MODULE` should point to your `settings.py` in your Django project.

Tornado handlers
----------------

To hook up Tornado handlers, use the common workflow:

```python
tornado_app = tornado.web.Application(
    [
        ('/hello-tornado', HelloHandler),
        ('.*', tornado.web.FallbackHandler, dict(fallback=container)),
    ])
```

Notice that in this example, all requests but `/hello-tornado` will be redirected to Django.

Requirements
------------

You'll obviously need the django and tornado Python-modules to run this demo ;-) You can install them quickly using `pip` and the provided `requirements.txt`. I recommend creating a virtual environment for every project you're working on.

`pip install -r requirements.txt`

Or install them manually:

```
pip install django
pip install tornado
```

