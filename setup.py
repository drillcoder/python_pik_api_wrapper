from setuptools import setup, find_packages

setup(name='python_pik_api_wrapper',
      version='1.1',
      description='Wrapper for the PIK Group website API',
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ],
      keywords='pik wrapper python',
      url='https://github.com/drillcoder/python_pik_api_wrapper',
      author='DrillCoder',
      author_email='nitrodrill@ya.ru',
      packages=find_packages(),
      install_requires=[
          'requests',
      ])
