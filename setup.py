# coding:utf-8
from setuptools import setup, find_packages

setup(
    name='getpass2',
    description='A better lib compared with standard "getpass" in Python, easier and simpler to use.',
    url='https://github.com/guoruibiao/getpass2',
    version='1.0.1',
    license='MIT',
    packages=find_packages(),
    entry_points = {
        "console_points": ['getpass = getpass2.getpass2:getpass']
    },
)