from setuptools import setup

setup(
    name='kneefinder',
    version='0.0.1',
    description='A simple tool to find the `knee` point of a 2-d curve.',
    url='',
    author='Vincenzo Lavorini',
    author_email='vincenzo.lavorini@protonmail.ch',
    license='BSD 2-clause',
    packages=['kneefinder'],
    install_requires=[
                      'numpy',
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
