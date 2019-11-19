from django.core.cache import caches
from django.conf import settings



def cache_file(upload, base_key=None, cache_name='default'):
    """
    Generates a key and stores the file at that key
    Returns the key for retrieving the file later
    """
    if not upload:
        raise Error('There is no upload file')
    upload.open()
    hsh = hash(upload.read(upload.DEFAULT_CHUNK_SIZE))
    cache = caches[cache_name]
    
    key = base_key or settings.get('CACHED_FILE_KEY', '')
    cache.set(settings.CACHED_FILE_KEY + hsh, upload, settings.CACHED_FILE_TIMEOUT)



def get_file(key, cache_name='default'):
    cache = caches[cache_name]
    return cache.get(key, None)
