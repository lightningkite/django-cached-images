# Django Cached Images

### Setup
Add app to installed apps in settings.py:
```python
INSTALLED_APPS = {
    ...
    'django-cached-images.cached_images',
    ...
}
```
Then add a url for the upload.
```python
from cached_images.views import CachedUploadView

urlpatterns = [
    ...
    url(r'^/upload/', CachedUploadView.as_view(),
    ...
]
```


