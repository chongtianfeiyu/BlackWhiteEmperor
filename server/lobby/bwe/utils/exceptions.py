#!/usr/bin/env python
# coding=utf-8


import json
from . import http_codes

class HTTPException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return json.dumps({"error_message": self.message})

except_dict={
    'BadRequestException': http_codes.BAD_REQUEST,
    'ForbiddenException': http_codes.FORBIDDEN,
    'NotFoundException': http_codes.NOT_FOUND,
    'UnauthorizedException': http_codes.UNAUTHORIZED,
    'ConflictException': http_codes.CONFLICT,
    'OverlimitException': http_codes.OVERLIMIT,
    'MethodNotAllowedException': http_codes.METHOD_NOT_ALLOWED,
    'InternalServerError': http_codes.INTERNAL_SERVER_ERROR,
}

bases = (HTTPException,)
for (eklass_name,code) in except_dict.items():
    attrs = {"code": code}
    eklass=type(eklass_name,bases,attrs)
    globals().update( {eklass_name: eklass } )
