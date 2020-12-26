from setuptools import setup

OPTIONS = {
    'iconfile': 'cloud.ico'
    }
setup(
    app=["utopia.py"],
    options={'py2app': OPTIONS},
setup_requires=["py2app"]
)