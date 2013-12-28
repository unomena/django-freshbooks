from setuptools import setup, find_packages

try:
    long_description = open('README', 'rt').read()
except IOError:
    long_description = ''

description = "A Freshbooks API app to use with Django"

setup(
    name='django-freshbooks',
    version='0.0.1',
    description=description,
    long_description = long_description,
    author='Euan Jonker',
    author_email='euan@unomena.com',
    license='License :: OSI Approved :: BSD License',
    url='http://github.com/unomena/django-freshbooks',
    packages = ['freshbooks'],
    install_requires = [
        'django<=1.6',
        'south<=0.8.4',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
    ],
)
