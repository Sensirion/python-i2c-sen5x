#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import importlib.metadata as metadata
from typing import Final

version: Final[str] = metadata.version("sensirion_i2c_sen5x")