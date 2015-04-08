from setuptools import setup, find_packages

setup(
    name='hover-ip-updater',
    version='1.0.0',
    author='Fernando Crespo',
    author_email='fernando82@gmail.com',
    packages=['hover'],
    #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='https://github.com/fcrespo82/dynamic-dns-on-hover',
    license=open('LICENSE.txt').read(),
    description='IP updater for Hover.com',
    long_description=open('README.rst').read(),
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
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
