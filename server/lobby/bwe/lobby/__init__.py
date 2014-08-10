#!/usr/bin/env python
# coding=utf-8


from flask import Flask
import os, json


app = Flask(__name__)
config = {}
config_file_name = os.path.dirname(__file__) + "/../../config.json"

with open(config_file_name) as f:
    config = json.loads(f.read())['dev']

app.config.update(**config['flask'])
