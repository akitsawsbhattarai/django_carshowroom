from django.shortcuts import redirect

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.user.is_authenticated)
        # if not request.user.is_authenticated:
        #     return redirect('/login') 
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response