django-tornado
==============

An example how to run django on Tornado. Simply run `run_tornado.py` and navigate your browser to

  [http://localhost:8080/hello-django](http://localhost:8080/hello-django)

or

  [http://localhost:8080/hello-tornado](http://localhost:8080/hello-tornado)

to see the HTTP-response from django respectively Tornado.

Settings
--------

You don't have to change anything to run this with your own djano project, but this line:

```python
os.environ['DJANGO_SETTINGS_MODULE'] = 'demosite.settings' # TODO: edit this
```

The `DJANGO_SETTINGS_MODULE` should point to your `settings.py` in your django project.

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

Notice that in this example, all requests but `/hello-tornado` will be redirected to django.
