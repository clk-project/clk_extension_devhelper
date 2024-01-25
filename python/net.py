#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

import click
from clk.decorators import group, option
from clk.log import get_logger

LOGGER = get_logger(__name__)


@group()
def net():
    "Some helpers with network stuffs"


@net.command()
@option("--port", default=8201, help="Start with this port and increment")
@option("--host", default="localhost", help="Where to listen to")
def available_port(port, host):
    "Find a port available to listen to"
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((host, port)) == 0:
                port = port + 1
            else:
                click.echo(port)
                break
