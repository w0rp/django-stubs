from typing import Any

from django.db import models
from django.http.request import HttpRequest

SITE_CACHE: Any

class SiteManager(models.Manager[Site, models.QuerySet[Site]]):
    def clear_cache(self) -> None: ...
    def get_by_natural_key(self, domain: str) -> Site: ...

class Site(models.Model):
    objects: SiteManager

    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    def natural_key(self) -> tuple[str]: ...

def clear_site_cache(sender: type[Site], **kwargs: Any) -> None: ...
