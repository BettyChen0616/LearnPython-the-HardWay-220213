try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'author': 'Betty',
    'url':'URL to get it at. ',
    'download_url':'Where to download it. ',
    'author_email':'1239870670@qq.com',
    'version': '0.1',
    'install_requires':['nose'],
    'packages':['ex47'],
    'script': [],
    'name': 'projectname'
}

setup(**config)
