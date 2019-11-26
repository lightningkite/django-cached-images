from rest_framework import serializers
from . import cache_file, get_file


class CachedFileField(serializers.FileField):
    def to_internal_value(self, key):
        upload = get_file(key)
        return super().to_internal_value(upload)
        

class CachedImageField(serializers.ImageField):
    def to_internal_value(self, key):
        upload = get_file(key)
        upload.seek(0)
        return super().to_internal_value(upload)


