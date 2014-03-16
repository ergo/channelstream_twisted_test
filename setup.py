import os
import sys
from setuptools import setup, find_packages


setup(name='channelstream',
      version='0.1',
      description='Websocket server supporting channels/users communication',
      classifiers=[
          'Intended Audience :: Developers'
          ],
      author='Marcin Lulek',
      author_email='info@webreactor.eu',
      license='BSD',
      zip_safe=True,
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.txt', '*.rst', '*.ini', '*.mak'],
          'channelstream': ['templates/*.jinja2', 'static'],
      },
      install_requires=[
          'twisted',
          'autobahn',
          'pyramid',
          'pyramid_jinja2',
      ],
      entry_points="""
      [console_scripts]
      channelstream = channelstream.start:cli_start
      """,
      )