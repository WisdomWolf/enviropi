from setuptools import setup, find_packages

import enviropi

setup(name='enviropi',
      version='0.1',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'enviro = enviropi.cli:main',
        ],
      },
      install_requires=[
        'envirophat',
        'smbus-cffi',
        'argh',
      ],
     )