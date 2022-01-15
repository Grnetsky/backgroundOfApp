from django.contrib.sessions.middleware import SessionMiddleware


class CustomSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        session_key = request.COOKIES.get('sessionid')
        if session_key is None:
            session_key = request.META.get('HTTP_X_TOKEN')
        request.session = self.SessionStore(session_key)