__author__ = 'acer'
#-*- coding: utf-8 -*-
#!/usr/bin/python

from common import exceptions

def main():
    a = "abc"
    try:
        b = int(a)
    except Exception as ex:
        raise exceptions.APIException(status="404", error_code="wrong")

if __name__ == "__main__":
    main()
