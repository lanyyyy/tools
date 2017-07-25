__author__ = 'acer'
#-*- coding: utf-8 -*-
#!/usr/bin/python

from common.messages import *

class APIException(Exception):

    def __init__(self, status="", error_code="400", message=NOT_FOUND_ERROR):
        Exception.__init__(self)
        self.message = message
        self.status = status
        self.error_code = error_code
        pass
