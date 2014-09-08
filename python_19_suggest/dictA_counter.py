#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)

import datetime
from time import mktime
try:
    import simplejson as sjson
except ImportError:
    import json

# 扩展json
class DateTimeEncoder(sjson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return sjson.JSONEncoder.default(self, obj)  # 返回父类的方法


d = datetime.datetime.now()
print sjson.dumps(d, cls=DateTimeEncoder)