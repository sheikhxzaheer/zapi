from rest_framework.response import Response

def zResponse(status, data=None, message=None, errorMessage=None):
    response_data = {'status': status}

    default_messages = {
        200: message if message else 'Success',
        201: 'Created',
        204: 'Deleted Successfllly',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        408: 'Request Timeout',
        413: 'Payload Too Large',
        500: 'Internal Server Error',
        502: 'Bad Gateway'
    }

    response_data['message'] = default_messages.get(status, 'Unknown Error')

    if data:
        response_data['data'] = data
    elif errorMessage:
        response_data['error'] = errorMessage

    return Response(data=response_data, status=status)