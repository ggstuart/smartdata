import os.path
from setuptools import setup, find_packages
#from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()


requires = ()#iterator of library names as strings

setup(
    name = "smartdata",
    version = "0.1",
    description = "A tool for extracting data from the smartspaces API",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP"
    ],
    author = "Graeme Stuart",
    author_email = "gstuart@dmu.ac.uk",
    url = "",
    packages = find_packages(),
    install_requires = requires,

    entry_points = {
        'console_scripts' : [
        'my_func = lib.main:main'         
        ]
        },
)
