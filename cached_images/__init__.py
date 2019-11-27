import io
from django.core.cache import caches
from django.core.files.base import ContentFile
from uuid import uuid4
from django.conf import settings



def cache_file(upload, base_key=None, cache_name='default', timeout=None):
    """
    Generates a key and stores the file at that key
    Returns the key for retrieving the file later
    """
    if not upload:
        raise Error('There is no upload file')
    cache = caches[cache_name]

    base_key = base_key or getattr(settings, 'CACHED_FILE_KEY', '')
    timeout = timeout or getattr(settings, 'CACHED_FILE_TIMEOUT', None)
    
    keys = []

    upload.open()
    for chunk in upload.chunks():
        hsh = hash(chunk)
        key = base_key + str(hsh)
        keys.append(key)
        if timeout:
            cache.set(key, chunk, timeout)
        else:
            cache.set(key, chunk)
    final_key = uuid4()
    initial = (upload.name, keys)
    if timeout:
        cache.set(final_key, initial, timeout)
    else:
        cache.set(final_key, initial)
    return final_key



def get_file(key, cache_name='default'):
    cache = caches[cache_name]
    filename, keys = cache.get(key, None)
    if not keys:
        return None

    c_file = ContentFile(b''.join(cache.get(key) for key in keys))
    c_file.name = filename
    return c_file
