from setuptools import setup


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='kneefinder',
    version='0.0.2',
    description='A simple tool to find the `knee` point of a 2-d curve.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vlavorini/kneefinder',
    author='Vincenzo Lavorini',
    author_email='vincenzo.lavorini@protonmail.ch',
    license='BSD 2-clause',
    packages=['kneefinder'],
    install_requires=[
                      'numpy',
                      'matplotlib'
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
