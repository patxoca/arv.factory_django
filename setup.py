from __future__ import unicode_literals

from setuptools import setup, find_packages

version = "0.1.2"

setup(
    name="arv.factory_django",
    version=version,
    description="Test fixtures replacement for django models.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
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
        "django>=1.8",
        # -*- Extra requirements: -*-
        "future",
    ],
    entry_points={
        # -*- Entry points: -*-
    },
)
