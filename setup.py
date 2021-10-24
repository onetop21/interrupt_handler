import sys
import os
from setuptools import setup, find_packages
from interrupt_handler import __version__

def main():
    # Read Description form file
    try:
        with open('README.rst') as f:
            description = f.read()
    except:
        print('Cannot find README.md file.', file=sys.stderr)
        description = "Interrupt Handling Utility for Python."

    setup(
      name='InterruptHandler',
      version=__version__,
      description='Interrupt Handling Library for Python.',
      long_description=description,
      author='Hyoil LEE',
      author_email='onetop21@gmail.com',
      license='MIT License',
      packages=find_packages(exclude=['.temp', '.test']),
      url='https://github.com/onetop21/interrupt_handler.git',
      zip_safe=False,
      python_requires='>=3.0',
      install_requires=[],
    )

if __name__ == '__main__':
    main()