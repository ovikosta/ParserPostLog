from setuptools import setup, find_packages

import parser

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='parserlog',
      version='0.1',
      author='OviKosta',
      author_email='ovikosta@gmail.com',
      url='https://github.com/ovikosta/parse-post-log',
      description='Parse post log.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['parserlog'],
      zip_safe=False)