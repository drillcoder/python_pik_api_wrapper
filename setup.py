from setuptools import setup, find_packages

import pik_wrapper

setup(name='python_pik_api_wrapper',
      version=pik_wrapper.__version__,
      description='Wrapper for the PIK Group website API',
      keywords='pik, wrapper, python',
      url='https://github.com/drillcoder/python_pik_api_wrapper',
      author='DrillCoder',
      author_email='nitrodrill@ya.ru',
      packages=find_packages(),
      install_requires=[
          'requests',
      ])
