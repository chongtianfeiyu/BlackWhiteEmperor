#!/usr/bin/env python
# coding=utf-8


from flask import request

from bwe.lobby import app
from bwe.utils import exceptions


@app.before_request
def oauth():
    if request.path != "/token":
        headers = request.headers
        if not headers.has_key("token"):
            raise exceptions.UnauthorizedException(\
                "You should indicate a token in HTTP Headers.")
        # TODO validate token

@app.errorhandler(exceptions.HTTPException)
def http_exception_handler(error):
    return str(error), error.code
