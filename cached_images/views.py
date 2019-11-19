from django.views import View
from django.http import JsonResponse
from . import cache_file

class CachedUploadView(View):
    """
    View for uploading files or images to the cache
    """
    def __init__(self, *args, **kwargs):
        self.base_key = kwargs.pop('base_key', None)
        self.cache_name = kwargs.pop('cache_name', None)
        super().__init__(*args, **kwargs)


    def post(self, request):
        upload = request.FILES['file']
        key = cache_file(upload, self.base_key, self.cache_name)
        return JsonResponse({'key': key})
