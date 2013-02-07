#!/usr/bin/env python
from distutils.core import setup

setup(
    name="mclp",
    version="1.0",
    description="A simple parser of Minecraft server logs",
    keywords="minecraft log parser",
    author="Steve Gattuso",
    license="MIT",
    author_email="steve@stevegattuso.me",
    url="http://github.com/stevenleeg/Minecraft-Log-Parser",
    scripts=["bin/mclp"]
)
