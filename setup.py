from setuptools import setup, find_packages

setup(
    name='hover-ip-updater',
    version='1.0.0',
    author='Fernando Crespo',
    author_email='fernando82@gmail.com',
    packages=['hover'],
    #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/HoverIPUpdater/',
    license=open('LICENSE.txt').read(),
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests",
        "docopt",
        "requests",
        "sys",
        "logging",
    ],
    entry_points={
        'console_scripts':
            ['hover-updater = hover.update:main',
        ]
    }
)
