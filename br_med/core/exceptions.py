from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


class VATRequestError(Exception):
    pass


class PeriodIsTooLargeException(Exception):
    pass


def handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, PeriodIsTooLargeException):
        data = {"error": "O período pesquisado é muito grande."}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    return response
