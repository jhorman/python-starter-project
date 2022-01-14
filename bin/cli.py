#!/usr/bin/env python

import logging
import os
import sys

import click

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

# noinspection PyUnresolvedReferences
import starter_project  # to force init


logger = logging.getLogger("starter_project.cli")


@click.group()
def cli():
    pass


if __name__ == "__main__":
    cli()
