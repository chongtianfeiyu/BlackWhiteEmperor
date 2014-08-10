#!/usr/bin/env python
# coding=utf-8

from rom import util
from bwe.lobby import config

util.set_connection_settings(**config['redis'])
