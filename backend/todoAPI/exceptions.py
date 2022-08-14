from rest_framework import status
from rest_framework.exceptions import APIException

class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'item not found.'
    default_code = 'not_found'


class MethodNotAllowed(APIException):
    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = 'Method "{method}" not allowed.'
    default_code = 'method_not_allowed'