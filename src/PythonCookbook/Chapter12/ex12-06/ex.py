#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-23
从XML DOM节点的子树中删除仅有空白符的文本节点
@author: CaiKnife
"""


def remove_whilespace_nodes(node):
    '''删除DOM节点中所有只含空白符的文本后裔'''
    remove_list = []
    for child in node.childNodes:
        if child.nodeType == dom.Node.TEXT_NODE and not child.data.strip():
            remove_list.append(child)
        elif child.hasChildNodes():
            remove_whilespace_nodes(child)

    for node in remove_list:
        node.parentNode.removeChild(node)
        node.unlink()
