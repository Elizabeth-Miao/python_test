#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 18:30:37
# @Author  : Nate Archibald (miaolei51886666@126.com)


try:
    import termios
    print 'hi'
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:  # 这里在最上面try成功会调用
    print 'fuck'
finally:  # 这里无论怎样都会调用
    print 'all'

import os







