#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Framework para Desenvolvimento de Agentes Inteligentes PADE

# The MIT License (MIT)

# Copyright (c) 2015 Lucas S Melo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pade',
      version='2.0.4',
      description='Framework para desenvolvimento de \
      sistemas multiagentes em Python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Lucas S Melo',
      author_email='lucassmelo@dee.ufc.br',
      package_data={'': ['*.html', '*.js', '*.css', '*.sqlite']},
      include_package_data=True,
      install_requires=['twisted===19.2.0',
                        'requests',
                        'pagan',
                        'alchimia===0.8.1',
                        'click===7.0',
                        'Flask-Bootstrap===3.3.7.1',
                        'Flask-Login===0.4.1',
                        'Flask-WTF===0.14.2',
                        'Flask-SQLAlchemy===2.3.2',
                        'Flask-Migrate===2.1.1',
                        'Flask-Script',
                        'Flask===1.0.2',
                        'terminaltables'],
      license='MIT',
      keywords='multiagent distributed systems',
      url='http://pade.readthedocs.org',
      packages=find_packages(),
      classifiers=[  
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'Topic :: Software Development :: Build Tools',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
      ],)
