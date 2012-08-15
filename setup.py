from setuptools import setup

version = __import__('specialization').__version__

setup(
    name = 'django-specialization',
    version = version,
    description = 'Primitive app for dynamically load templates from different folders based on hostname',
    author = 'Emil Eriksson, CodeMill AB',
    author_email = 'opensource@codemill.se',
    url = 'http://github.com/asheidan/django-specialization',
    packages = ['specialization'],
    install_requires = [
        'django>=1.3',
    ],
)
