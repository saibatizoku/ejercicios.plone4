# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ejercicios.plone4',
        version=version,
        description="Ejercicios para desarrollar con Plone 4",
        long_description=open("README.txt").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read(),
        # Get more strings from
        # http://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            "Framework :: Plone",
            "Programming Language :: Python",
            ],
        keywords='',
        author='Joaquin Rosales',
        author_email='globojorro@gmail.com',
        url='http://svn.plone.org/svn/collective/',
        license='GPL',
        packages=find_packages(exclude=['ez_setup']),
        namespace_packages=['ejercicios'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'setuptools',
            # -*- Extra requirements: -*-
            'plone.app.dexterity>=1.0.3',
            'plone.app.referenceablebehavior',
            'plone.app.relationfield',
            ],
        extras_require={
            'test': ['plone.app.testing'],
            },
        entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
