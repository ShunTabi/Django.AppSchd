from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("AppSchd/", include("AppSchd.urls.urlsAppSchd")),
    path("AppBook/", include("AppBook.urls.urlsAppBook")),
]
