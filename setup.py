#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import setuptools
setuptools.setup(
    name = "ichisaki",
    version = "0.0.8",
    description = "A Simple Toolkit just for FUN",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/sandyzikun/ichisaki.git",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ],
    packages = setuptools.find_packages(), #["icsk"],
    install_requires = ["numpy>=1.14.3"], # Actually it needs Functions in `np.linalg` which is in NumPy>=1.9.3
    )
