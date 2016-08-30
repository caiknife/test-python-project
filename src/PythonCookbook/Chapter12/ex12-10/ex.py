#!/usr/bin/python
# coding: UTF-8
"""
Created on 2012-11-23
用SAX合并连续的文本事件
@author: CaiKnife
"""

from xml.sax.saxutils import XMLFilterBase


class text_normalize_filter(XMLFilterBase):
    """SAX过滤器，确保连续的文本节点被合并为一个"""

    def __init__(self, upstream, downstream):
        XMLFilterBase.__init__(self, upstream)
        self._downstream = downstream
        self._accumulator = []

    def _complete_text_node(self):
        if self._accumulator:
            self._downstream.characters(''.join(self._accumulator))
            self._accumulator = []

    def characters(self, text):
        self._accumulator.append(text)

    def ignorableWhitespace(self, ws):
        self._accumulator.append(ws)
