import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Improcpy",
    version="0.0.4",
    author="Ranveer Aggarwal",
    author_email="ranveeraggarwal@gmail.com",
    description=("An image processing ensemble in Python"),
    license="GPL 3.0",
    keywords="improcpy image processing",
    packages=['improcpy'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL 3.0 License",
    ],
)
