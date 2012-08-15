from django.contrib.sites.models import get_current_site

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_host():
    return getattr(_thread_locals, 'specialization_host', None)

class SpecializationMiddleware:
    def process_request(self, request):
        #print repr(request)
        host = request.META.get('HTTP_HOST','').split(':')[0]
        _thread_locals.specialization_host = host
