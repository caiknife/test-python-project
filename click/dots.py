#!/usr/bin/env python
# coding:utf8

import click


@click.command()
@click.option("--n", default=5, help="Repeat times.")
def dots(n):
    click.echo('.' * n)


if __name__ == "__main__":
    dots()
