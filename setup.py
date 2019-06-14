from setuptools import find_packages, setup
from configparser import ConfigParser

long_description = "Python sdk "
config = ConfigParser()
config.read("VERSION.ini")
PYTHON_SDK_VERSION = config['VERSION_INFO']['package_version']

setup(
    name='paytm-pg',
    version=PYTHON_SDK_VERSION,
    author='avneesh gupta',
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
