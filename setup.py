from __future__ import unicode_literals

from setuptools import setup, find_packages

version = "0.1.4"

setup(
    name="arv.factory_django",
    version=version,
    description="Test fixtures replacement for django models.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2",
        "Framework :: Django :: 3",
        "Framework :: Django :: 4",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="",
    author="Alexis Roda",
    author_email="alexis.roda.villalonga@gmail.com",
    url="https://github.com/patxoca/arv.factory_django",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["arv"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "arv.factory",
        "django>=1.10",
        # -*- Extra requirements: -*-
        "future",
    ],
    entry_points={
        # -*- Entry points: -*-
    },
)
