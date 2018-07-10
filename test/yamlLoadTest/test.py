#-*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'lanyyyy'

import yaml
import ytools
from yaml import YAMLObject
from collections import OrderedDict

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def main():
    """测试yaml数据顺序是否一致"""
    # 如果读取后为list，则是有序，比如在first.yaml中的key是以“-”开头，读取后为list
    filepath = "first.yaml"
    with open(filepath, "r+") as fd:
        data = yaml.load(fd)
        print data

    # 如果读取后为json，则是无无序，比如在second.yaml，读取后为json，顺序无法保证
    filepath = "second.yaml"
    with open(filepath, "r+") as fd:
        data = yaml.load(fd)
        print data

    # 测试使用ytools，只是格式化输出，无什么明显意义
    x = ytools.dump(filepath)
    print x

    # 测试YAMLObject，但是并无用处
    data = YAMLObject.yaml_dumper(filepath)
    print data

    # 测试OrderedDict，是完全可以正常的进行初始化
    print u"测试OrderedDict读取yaml文件数据"
    with open("first.yaml", "r+") as fd:
        data = ordered_load(fd, yaml.SafeLoader)
        print data
    with open("second.yaml", "r+") as fd:
        data = ordered_load(fd, yaml.SafeLoader)
        print data

    # 再将OrderedDict转化为dict，可以成功转化
    dictdata = dict(data)
    print dictdata

    # 取list部分转为json：
    print u"取list部分转化为json"
    with open("first.yaml", "r+") as fd:
        data = ordered_load(fd, yaml.SafeLoader)
        print data
        # 判断是list还是OrderedDict
        if (isinstance(data, list)):
            data0 = dict(data.pop(0))
            print "list: ", data0
        if (isinstance(data, OrderedDict)):
            data1 = dict(data.popitem(last=False))
            print "OrderedDict开始: ",  data1

    # 取OrderedDict部分转为json：
    print u"取OrderedDict部分转化为json"
    with open("second.yaml", "r+") as fd:
        data = ordered_load(fd, yaml.SafeLoader)
        print data
        # 判断是list还是OrderedDict
        if (isinstance(data, list)):
            data0 = dict(data.pop(0))
            print "list: ", data0
        if (isinstance(data, OrderedDict)):
            data1 = dict(data.popitem(last=False))
            print "OrderedDict开始: ",  data1

if __name__ == "__main__":
    main()