from setuptools import setup, find_packages

import parser

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='parser-post-log',
      version=parser.__version__,
      url='https://github.com/ovikosta/parse-post-log',
      license='MIT',
      author='OviKosta',
      author_email='ovikosta@gmail.com',
      description='Parse post log.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(exclude=['tests']),
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ])