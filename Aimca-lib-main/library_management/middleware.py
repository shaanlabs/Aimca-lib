from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
import re

class LoginRequiredMiddleware:
    """
    Require login for all pages except login/logout, admin, and static files.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            re.compile(r'^admin/'),
            re.compile(r'^static/'),
            re.compile(r'^accounts/login/?$'),
            re.compile(r'^accounts/logout/?$'),
            re.compile(r'^accounts/password'),
            re.compile(r'^about_us/?$'),  # Allow public access to About Batch-26 page
            re.compile(r'^about/?$'),     # Also allow /about/ for About Batch-26 page
        ]

    def __call__(self, request):
        path = request.path_info.lstrip('/')
        if not request.user.is_authenticated:
            if not any(m.match(path) for m in self.exempt_urls):
                return redirect(settings.LOGIN_URL + '?next=' + request.path)
        return self.get_response(request)
