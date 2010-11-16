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
        'static/css/sass/compass/*.sass',
        'static/css/sass/compass/core/*.sass',
        'static/css/sass/compass/core/css3/*.sass',
        'static/css/sass/compass/core/reset/*.sass',
        'static/css/sass/compass/core/utilities/*.sass',
        'static/css/sass/compass/core/utilities/general/*.sass',
        'static/css/sass/compass/core/utilities/links/*.sass',
        'static/css/sass/compass/core/utilities/lists/*.sass',
        'static/css/sass/compass/core/utilities/sprites/*.sass',
        'static/css/sass/compass/core/utilities/tables/*.sass',
        'static/css/sass/compass/core/utilities/text/*.sass',
        'static/css/sass/frameworks/*.sass',
        'static/css/sass/frameworks/susy/*.sass',
        'static/css/sass/frameworks/graphpaper/*.sass',
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