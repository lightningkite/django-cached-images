from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import cache_file

@method_decorator(csrf_exempt, name='dispatch')
class CachedUploadView(View):
    """
    View for uploading files or images to the cache
    """
    base_key = None
    cache_name = 'default'

    def post(self, request):
        upload = request.FILES['file']
        key = cache_file(upload, self.base_key, self.cache_name)
        return JsonResponse({'key': key})
