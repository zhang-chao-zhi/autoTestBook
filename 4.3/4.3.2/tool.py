# -*- coding: utf-8 -*-
def load_cheers():
    # 这个函数会被mock的patch对象替换，并不会真正调用，这个函数在实际工程中可能是调用栈复杂的业务块或者网络请求复杂的服务
    # 这里只是为了演示，所以看起来只是个简单返回，实际工作中会复杂得多。
    return "Come on,Chengdu!"