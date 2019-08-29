from django.http import JsonResponse

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        print(exception)
        return JsonResponse({'result':'error','message':str(exception)}, status=500)
