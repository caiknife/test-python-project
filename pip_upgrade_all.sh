#!/usr/bin/env bash
pip list --outdated | cut -d " " -f 1 | xargs -n1 pip install -U