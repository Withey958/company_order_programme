from setuptools import setup

APP = ['orderprog.py']
DATA_FILES = ['/Users/lukewithey/PycharmProjects/crumpetorium_order_list/images/crumpetorium_logo.jpg']
OPTIONS = {
    'iconfile':'hnet.com-image.ico', #choose a new iconfile
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)