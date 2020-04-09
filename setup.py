from setuptools import setup

APP = ['orderprog.py']
DATA_FILES = ['Thrive-logo-512p.gif']
OPTIONS = {
    'iconfile':'hnet.com-image.ico',
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)