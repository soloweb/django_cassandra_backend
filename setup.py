import os
from setuptools import setup

from django_cassandra import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django_cassandra",
    version = __version__,
    author = "Rob Vaterlaus",
    author_email = "https://github.com/vaterlaus",
    description = ("Django backend for the Cassandra database."),
    license = "Unknown",
    keywords = "cassandra pycassa django orm backend",
    url = "https://github.com/vaterlaus/django_cassandra_backend",
    packages = [
        'django_cassandra',
        'django_cassandra.db',
    ],
    install_requires=['cassandra', 'thrift', 'django', 'djangotoolbox'],
    long_description=read('README.txt'),
    classifiers=[
       "Framework :: Django",
       "Programming Language :: Python",
       "Programming Language :: Python :: 2.7",
       "Topic :: Database",
       "Topic :: Database :: Database Engines/Servers",
       "Topic :: Internet",
       "Topic :: Utilities",
       "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)