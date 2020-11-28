from rest_framework import response, status


def handle_err(func):
    """ If view failed, decorator returns
        readable error to the client
    """
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            msg = {
                'error' : "Something went wrong."
            }
            return response.Response(
                msg, status=status.HTTP_400_BAD_REQUEST
            )
    wrap.__doc__=func.__doc__
    wrap.__name__=func.__name__
    return wrap