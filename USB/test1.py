#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Author:chenpengrui
@File:test1.py
@Time:2021/05/07
@Description:
"""

import usb.util
import sys

devlist = usb.core.find(find_all=True)
for d in devlist:
    if (d.idVendor == 0x046d) & (d.idProduct == 0xc08b):
        print(d)
