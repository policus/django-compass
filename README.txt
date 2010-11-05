## About ##

django-compass is a port of [Compass](http://compass-style.org) for use in
Django 1.3+ projects. It's a simple app containing static files for Compass and
the Susy framework. Requires a sass compiler like [django-css](https://github.com/dziegler/django-css/) to be useful.
## Assumptions ##

1. You have a sass compiler installed
2. You store your css in settings.STATICFILE_ROOT + 'css/'
3. You store your sass in settings.STATICFILE_ROOT + 'css/sass/'

## Installation ##

1. Add 'compass' to INSTALLED_APPS
2. Make sure your have configured django.contrib.staticfiles in your settings
	

	import os
	here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)
	STATICFILES_ROOT = here('static')
	STATICFILES_FINDERS = (
	    "django.contrib.staticfiles.finders.FileSystemFinder",
	    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
	)

3. Run ./manage.py collectstatic
4. Compile your SASS with something like [django-css](https://github.com/dziegler/django-css/)