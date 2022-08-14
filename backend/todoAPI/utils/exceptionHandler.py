from rest_framework.views import exception_handler

import sys

def custom_exception_handler(exc, context=None):

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response and rename detail to error
    if response is not None:
        response.data['status_code'] = response.status_code

    return response