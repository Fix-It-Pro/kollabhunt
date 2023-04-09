import threading

GLOBAL_REQUEST_KEEPER = threading.local()


class GlobalRequestMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        GLOBAL_REQUEST_KEEPER.request = request
        try:
            return self.get_response(request)
        except Exception as e:
            print(str(e))
        finally:
            if hasattr(GLOBAL_REQUEST_KEEPER, "request"):
                del GLOBAL_REQUEST_KEEPER.request


def get_request():
    try:
        return GLOBAL_REQUEST_KEEPER.request
    except AttributeError:
        return None
