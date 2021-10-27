from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.db import DatabaseError


def common_exception_handler(exc, context):
    response = exception_handler(exc, context)
    # 在此处补充自定义的异常处理
    if response is None:
        view = context['view']
        print('[%s]: %s' % (view, exc))
        if isinstance(exc, DatabaseError):
            response = Response({'code': 401, 'detail': '数据库错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, ZeroDivisionError):
            response = Response({'code': 402, 'detail': '除以0的错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        elif isinstance(exc, NameError):
            response = Response({'code': 403, 'detail': '变量未定义被引用'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        else:
            response = Response({'code': 666, 'detail': '未知错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
