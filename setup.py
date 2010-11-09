from distutils.core import setup
import os

setup(
    name='django-compass',
    version='0.1',
    description='django-compass is a port of Compass (http://compass-style.org/) for use with Django 1.3+',
    long_description=open('README.markdown').read(),
    author='Policus',
    author_email='Alex Cabrera <alex@policus.com>',
    url='https://github.com/policus/django-compass',
    packages=['compass',],
    package_data={'compass':[
        'static/css/sass/_compass.sass',
        'static/css/sass/compass/*.sass',
        'static/css/sass/compass/css3/*.sass',
        'static/css/sass/compass/reset/*.sass',
        'static/css/sass/compass/utilities/*.sass',
        'static/css/sass/compass/utilities/general/*.sass',
        'static/css/sass/compass/utilities/links/*.sass',
        'static/css/sass/compass/utilities/lists/*.sass',
        'static/css/sass/compass/utilities/sprites/*.sass',
        'static/css/sass/compass/utilities/tables/*.sass',
        'static/css/sass/compass/utilities/text/*.sass',
        'static/css/sass/frameworks/_susy.sass',
        'static/css/sass/frameworks/susy/*.sass',
    ]},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)