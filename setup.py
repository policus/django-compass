from distutils.core import setup
import os
import logging
# Compile the list of packages available, because disutils doesn't have an
# easy way to do this
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

# Snippet from http://django-registration.googlecode.com/svn/trunk/setup.py
for dirpath, dirnames, filenames in os.walk('compass'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath # Strip "registration/" or "registration\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
            
setup(
    name='django-compass',
    version='0.1',
    description='django-compass is a port of Compass (http://compass-style.org/) for use with Django 1.3+',
    long_description=open('README.markdown').read(),
    author='Policus',
    author_email='Alex Cabrera <alex@policus.com>',
    url='https://github.com/policus/django-compass',
    packages=packages,
    data_files=data_files,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ]
)