# Setup.py

from setuptools import setup


setup(name='tacklebox',
      version='0.1',
      description='portable configuration manager',
      url='http://github.com/OmerShapira/Tacklebox',
      author='Omer Shapira',
      author_email='info@omershapira.com',
      license='MIT',
      packages=['tacklebox'],
      install_requires=[
          'toml',
      ],
      zip_safe=False)
