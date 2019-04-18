from setuptools import setup, find_packages

import parser

setup(name='parser-post-log',
      version=parser.__version__,
      url='https://github.com/ovikosta/parse-post-log',
      license='MIT',
      author=parser.__author__,
      author_email='ovikosta@gmail.com',
      description='Parse post log.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=[],
      test_suite='')