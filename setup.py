from setuptools import find_packages, setup
from paytmpg.pg.constants.LibraryConstants import LibraryConstants

long_description = "Python sdk "

setup(
    name='paytm-pg',
    version=LibraryConstants.PYTHON_SDK_VERSION,
    author='avneesh gupta',
    author_email='avneesh.gupta@paytm.com',
    description="Merchant util library which provide payment, payment status, refund and refund status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/avneesh111995/paytm-pg-python-sdk/",
    packages=find_packages(),
    install_requires=["requests", "pycryptodome"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
