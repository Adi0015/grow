# setup.py

from setuptools import setup, find_packages

setup(
    name='grow',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'grow = grow.__init__:main'
        ]
    }
)
