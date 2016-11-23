#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

from djangocms_inline_comment import __version__


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname), 'r').read()
    except IOError:
        return u''

setup(
    name='djangocms-inline-comment',
    version=__version__,
    author='arteria GmbH',
    author_email='admin@arteria.ch',
    url='https://github.com/arteria/djangocms-inline-comment',
    license='The MIT License',
    description=('Add comments to the django CMS structure board.'),
    long_description=read('README.rst'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().split('\n'),
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
