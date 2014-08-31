#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


def info(obj, spacing=10, collapse=1):
    '''
    what the...
    '''
    methodlist = [method for method in dir(obj) if callable(getattr(obj, method))]
    processfunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" % (method.ljust(spacing), processfunc(str(getattr(obj, method).__doc__))) for method in methodlist])



if __name__ == '__main__':
    print type(info.__doc__)
    print str(info.__doc__)

    # d = {}
    # print [ds for ds in dir(d) if '__' not in ds]
    li = [1,2,3]
    myappend = getattr(li, 'append')








