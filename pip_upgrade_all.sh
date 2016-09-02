#!/usr/bin/env bash
pip list --outdated | cut -d " " -f 1 | xargs pip install -U