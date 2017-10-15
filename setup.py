#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="kademlia_iic2523",
    version="0.0.1",
    author="Vicente Dragicevic",
    url="http://github.com/vdrg/kademlia-iic2523",
    packages=find_packages(),
    install_requires=[
        "kademlia==1.0",
        "rpcudp==3.0.0"
    ],
    dependency_links=[
        #  "git+https://github.com/bmuller/rpcudp@python3.5",
        "https://github.com/bmuller/rpcudp/zipball/python3.5#egg=rpcudp-3.0.0",
        "https://github.com/vdrg/kademlia/zipball/python3.5#egg=kademlia-1.0"
        #  "git+ssh://git@github.com/vdrg/kademlia.git@python3.5#egg=kademlia-1.0"
    ]
)
