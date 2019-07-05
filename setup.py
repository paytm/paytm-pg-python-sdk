from setuptools import find_packages, setup
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from sys import version_info
from os.path import abspath

long_description = "Python sdk "
config = configparser.ConfigParser()
file_path = '/'.join(abspath(__file__).split('/')[:-1])

file_abs_path = file_path + "/paytmpg/VERSION.ini"
config.read(file_abs_path)

if version_info[0] < 3:
    PYTHON_SDK_VERSION = config.get('VERSION_INFO', 'package_version')
else:
    PYTHON_SDK_VERSION = config['VERSION_INFO']['package_version']

setup(
    name='paytm-pg',
    package_data={'paytmpg': ['VERSION.ini']},
    version=PYTHON_SDK_VERSION,
    author='Avneesh Gupta',
    author_email='pgplus.tyche@paytm.com',
    description="Merchant util library which provide payment, payment status, refund and refund status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paytm/paytm-pg-python-sdk",
    packages=find_packages(),
    install_requires=["requests", "pycryptodome"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
