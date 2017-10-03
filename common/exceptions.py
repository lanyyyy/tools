__author__ = 'acer'
#-*- coding: utf-8 -*-
#!/usr/bin/python

from common.messages import *

class APIException(Exception):

    def __init__(self, status="", error_code="", message=NOT_FOUND_ERROR):
        Exception.__init__(self)
        self.message = message
        self.status = status
        self.error_code = error_code
        pass

    def __str__(self):
        return "An Error Occured: Status: %s; Error_code: %s; Msg: %s" %\
               (self.status, self.error_code, self.message)
