# coding=utf-8

from os import path

ROOT_DIR = path.dirname(path.dirname(__file__))


# 获取文件绝对路径
def resolve(name):
    return path.join(ROOT_DIR, name)
