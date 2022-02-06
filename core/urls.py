from django.contrib import admin
from django.urls import path, include

import os

urlpatterns = [
    path(f"{os.environ.get('ADMIN_PAGE_SLUG')}/", admin.site.urls),
    path("", include("api.urls")),
]
